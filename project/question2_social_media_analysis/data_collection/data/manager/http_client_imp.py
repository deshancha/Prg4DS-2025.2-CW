import aiohttp
import asyncio
from domain.manager.ihhtp_client import IHttpClient
from domain.model.api_response import ApiResponse
from util.logger import Logger

class HttpClientImp(IHttpClient):
    def __init__(self, timeout = 3, maxRetry = 3):
        self.timeout = timeout
        self.maxRetries = maxRetry
        self.backOff = 0.2

    async def get(self, url: str) -> ApiResponse:
        return await self._retry_async(url)
        
    async def _request(self, url: str) -> ApiResponse:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=self.timeout)) as session:
            async with session.get(url) as response:
                text = await response.text()
                return ApiResponse(status_code=response.status, body=text)
        
    async def _retry_async(self, url: str):
        attempt = 0
        while attempt < self.maxRetries:
            try:
                response = await self._request(url)

                if(attempt>0):
                    Logger.verbose(f"Success After failured, Attempt: {attempt}/{self.maxRetries}, url:{url}")

                return response
            except Exception as e:
                attempt += 1
                slepTime = min(self.backOff * (2 ** (attempt - 1)), 2.0)
                Logger.warn(f"Request Failed!, Attempt: {attempt}/{self.maxRetries} after {slepTime} secs")
                await asyncio.sleep(slepTime)

        Logger.error(f"Permanent Failure, url:{url}")
        return ApiResponse(status_code=-1, body=f"Failed with max retry: {self.maxRetries}")
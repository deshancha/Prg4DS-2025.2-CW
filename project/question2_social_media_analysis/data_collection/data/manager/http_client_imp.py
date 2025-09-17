import aiohttp
import asyncio
from domain.manager.ihhtp_client import IHttpClient
from domain.model.api_response import ApiResponse

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
                return await self._request(url)
            except Exception as e:
                attempt += 1
                slepTime = min(self.backOff * (2 ** (attempt - 1)), 2.0)
                print(f"Request Failed!, Attempt: {attempt}/{self.maxRetries} after {slepTime} secs")
                await asyncio.sleep(slepTime)
        return ApiResponse(status_code=-1, body=f"Failed with max retry: {self.maxRetries}")
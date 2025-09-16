import aiohttp
from domain.manager.ihhtp_client import IHttpClient
from domain.model.api_response import ApiResponse

class HttpClientImp(IHttpClient):
    def __init__(self, timeout = 3):
        self.timeout = timeout

    async def get(self, url: str) -> ApiResponse:
        try:
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=self.timeout)) as session:
                async with session.get(url) as response:
                    text = await response.text()
                    return ApiResponse(status_code=response.status, body=text)
        except Exception as e:
            return ApiResponse(status_code=-1, body=str(e))
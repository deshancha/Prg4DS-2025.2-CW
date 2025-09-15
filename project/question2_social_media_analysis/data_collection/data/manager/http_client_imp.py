import requests
from requests.exceptions import RequestException
from domain.manager.ihhtp_client import IHttpClient
from domain.model.api_response import ApiResponse

class HttpClientImp(IHttpClient):
    def __init__(self, timeout = 3):
        self.timeout = timeout

    def get(self, url: str) -> ApiResponse:
        try:
            resp = requests.get(url, timeout=self.timeout)
            return ApiResponse(status_code=resp.status_code, body=resp.text)
        except RequestException as e:
            return ApiResponse(status_code=-1, body=str(e))
from abc import ABC, abstractmethod
from domain.model.api_response import ApiResponse

class IHttpClient(ABC):
    @abstractmethod
    def get(url) -> ApiResponse:
        pass
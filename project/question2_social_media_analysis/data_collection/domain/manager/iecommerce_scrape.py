from abc import ABC, abstractmethod
from typing import List
from domain.model.product_detail import ProductDetail

class IECommerceScrape(ABC):
    @abstractmethod
    async def collectData(self, pageCount: int) -> List[ProductDetail]:
        pass
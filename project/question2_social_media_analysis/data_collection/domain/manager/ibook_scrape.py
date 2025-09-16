from abc import ABC, abstractmethod
from typing import List
from domain.model.book_detail import BookDetail

class IBookScrape(ABC):
    @abstractmethod
    async def collectData(self, pageCount: int) -> List[BookDetail]:
        pass
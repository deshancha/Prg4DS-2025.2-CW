from abc import ABC, abstractmethod
from typing import List, TypeVar

T = TypeVar("T")

class ISaveFile(ABC):
    @abstractmethod
    async def saveJson(self, data: List[T], filename: str):
        pass
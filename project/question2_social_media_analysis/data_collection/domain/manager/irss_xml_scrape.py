from abc import ABC, abstractmethod
from typing import List
from domain.model.rss_element import RSSElement

class IRSSXMLScrape(ABC):
    @abstractmethod
    async def collectData(self) -> List[RSSElement]:
        pass
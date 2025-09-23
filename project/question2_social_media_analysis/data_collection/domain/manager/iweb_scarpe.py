from abc import ABC, abstractmethod
from typing import List, Callable, TypeVar
from bs4 import BeautifulSoup as BS

T = TypeVar("T")

class IWebScarape(ABC):
    @abstractmethod
    def getFromHtml(
        htmlText:str,
        selector: str,
        elementMapper: Callable[[BS, str], T]
    ) -> List[T]:
        pass

        def getFromHtmlSingle(self,
                                htmlText: str,
                                elementMapper: Callable[[BS], T],
                                selector: str | None = None) -> T | None:
            pass

    def getFromXml(self,
                    xmlContent:str,
                    selector: str,
                    elementMapper: Callable[[BS, str], T]) -> List[T]:
        pass
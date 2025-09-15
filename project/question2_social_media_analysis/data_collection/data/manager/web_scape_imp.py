from domain.manager.iweb_scarpe import IWebScarape, T
from bs4 import BeautifulSoup as BS
from typing import List, Callable

class WebScrapeImp(IWebScarape):
    def getFromHtml(self,
                    htmlText:str,
                    selector: str,
                    elementMapper: Callable[[BS, str], T]) -> List[T]:
        soup = BS(htmlText, 'html.parser')
        elements = soup.select(selector)
        return [elementMapper(elm) for elm in elements]
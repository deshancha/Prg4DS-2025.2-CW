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
    
    def getFromHtmlSingle(self, htmlText: str, selector: str, elementMapper: Callable[[BS], T]) -> T | None:
        soup = BS(htmlText, 'html.parser')
        element = soup.select_one(selector)
        if element:
            return elementMapper(element)
        return None
    
    def getFromXml(self,
                    xmlContent:str,
                    selector: str,
                    elementMapper: Callable[[BS, str], T]) -> List[T]:
        soup = BS(xmlContent, 'lxml-xml')
        elements = soup.find_all(selector)
        return [elementMapper(elm) for elm in elements]
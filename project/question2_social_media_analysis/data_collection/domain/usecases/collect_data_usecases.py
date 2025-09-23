from domain.manager.ibook_scrape import IBookScrape
from domain.manager.iecommerce_scrape import IECommerceScrape
from domain.manager.irss_xml_scrape import IRSSXMLScrape

class CollectDataUseCases:
    def __init__(
            self,
            iBookScrape: IBookScrape,
            iEcommerceScrape: IECommerceScrape,
            irssScrape: IRSSXMLScrape):
        self.iBookScrape = iBookScrape
        self.iEcommerceScrape = iEcommerceScrape
        self.irssScrape = irssScrape

    async def booksScrape(self, pageCount: int):
        return await self.iBookScrape.collectData(pageCount)
    
    async def eCommerceScrape(self, pageCount: int):
        return await self.iEcommerceScrape.collectData(pageCount)
    
    async def rssScrape(self):
        return await self.irssScrape.collectData()
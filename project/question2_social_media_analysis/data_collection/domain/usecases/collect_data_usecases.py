from domain.manager.ibook_scrape import IBookScrape
from domain.manager.iecommerce_scrape import IECommerceScrape

class CollectDataUseCases:
    def __init__(
            self,
            iBookScrape: IBookScrape,
            iEcommerceScrape: IECommerceScrape):
        self.iBookScrape = iBookScrape
        self.iEcommerceScrape = iEcommerceScrape

    async def booksScrape(self, pageCount: int):
        return await self.iBookScrape.collectData(pageCount)
    
    async def eCommerceScrape(self, pageCount: int):
        return await self.iEcommerceScrape.collectData(pageCount)
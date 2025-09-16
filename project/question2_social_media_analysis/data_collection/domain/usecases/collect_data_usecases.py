from domain.manager.ibook_scrape import IBookScrape

class CollectDataUseCases:
    def __init__(
            self,
            iBookScrape: IBookScrape):
        self.iBookScrape = iBookScrape

    async def booksScrape(self, pageCount: int):
        return await self.iBookScrape.collectData(pageCount)
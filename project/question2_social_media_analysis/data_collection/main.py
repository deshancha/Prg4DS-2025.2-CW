import asyncio
from data.manager.http_client_imp import HttpClientImp
from domain.manager.ihhtp_client import IHttpClient
from domain.manager.iweb_scarpe import IWebScarape
from data.manager.web_scape_imp import WebScrapeImp
from domain.usecases.collect_data_usecases import CollectDataUseCases

from data.manager.book_scrape_imp import BookScrapeImp

from di.container import Container

async def collect_data(fetchCount=1):
    container = Container()
    useCases = container.useCases()

    booksList = await useCases.booksScrape(pageCount=fetchCount)

    print(f"Total: {len(booksList)}")
    
if __name__ == "__main__":
    asyncio.run(collect_data(fetchCount=2))


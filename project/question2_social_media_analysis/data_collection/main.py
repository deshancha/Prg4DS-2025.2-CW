import asyncio
from data.manager.http_client_imp import HttpClientImp
from domain.manager.ihhtp_client import IHttpClient
from domain.manager.iweb_scarpe import IWebScarape
from data.manager.web_scape_imp import WebScrapeImp
from domain.usecases.collect_data_usecases import CollectDataUseCases

from data.manager.book_scrape_imp import BookScrapeImp

async def collect_data(fetchCount=1):
    client: IHttpClient = HttpClientImp(timeout=5)
    scraper: IWebScarape = WebScrapeImp()

    useCases = CollectDataUseCases(
        iBookScrape = BookScrapeImp(client=client, scraper=scraper))

    booksList = await useCases.booksScrape(pageCount=fetchCount)

    print(f"Total: {len(booksList)}")
    
if __name__ == "__main__":
    asyncio.run(collect_data(fetchCount=2))


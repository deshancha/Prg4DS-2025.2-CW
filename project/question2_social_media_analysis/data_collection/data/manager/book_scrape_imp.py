import asyncio
from bs4 import BeautifulSoup as BS
from domain.manager.ihhtp_client import IHttpClient
from domain.manager.iweb_scarpe import IWebScarape
from domain.manager.ibook_scrape import IBookScrape
from domain.components.app_const import AppConst
from domain.model.api_response import ApiResponse
from domain.model.product import Product
from typing import List
from domain.model.book_detail import BookDetail

SCRAPE_HOST = "https://books.toscrape.com"
PAGE_URL_TEMPLATE = SCRAPE_HOST + "/catalogue/page-{}.html"
BOOK_URL_TEMPLATE = SCRAPE_HOST + "/catalogue/{}"

def responseOk(response: ApiResponse):
    return response.status_code == AppConst.HTTP_OK

# callback param calls from scraper, this would parse product html
def _mapProduct(element: BS) -> Product:
    aTag = element.find("a")
    imgTag = element.find("img")
    href = aTag["href"] if aTag else ""
    title = imgTag.get("alt") if imgTag else ""
    return Product(title=title, url=href)

class BookScrapeImp(IBookScrape):
    def __init__(self, scraper: IWebScarape, client: IHttpClient,):
        self.scraper = scraper
        self.client = client

    async def _fetchPage(self, pageNumber: int):
        pageUrl = PAGE_URL_TEMPLATE.format(pageNumber)
        response = await self.client.get(pageUrl)

        if not responseOk(response):
            return []

        products = self.scraper.getFromHtml(response.body, "article.product_pod", _mapProduct)
        for product in products:
            print(f"Page:{pageNumber} {product.title}")
        # TODO: Fetch books here
        return []


    async def collectData(self, pageCount: int) -> List[BookDetail]:
        pageTasks = []
        for i in range(1, pageCount + 1):
            pageTasks.append(asyncio.create_task(self._fetchPage(i)))

        booksList = await asyncio.gather(*pageTasks)
        
        return booksList


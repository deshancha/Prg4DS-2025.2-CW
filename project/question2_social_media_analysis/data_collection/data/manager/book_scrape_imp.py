import asyncio
import random
from typing import List
from itertools import chain

from bs4 import BeautifulSoup as BS
from domain.manager.ihhtp_client import IHttpClient
from domain.manager.iweb_scarpe import IWebScarape
from domain.manager.ibook_scrape import IBookScrape
from domain.components.app_const import AppConst
from domain.model.api_response import ApiResponse
from domain.model.book_meta import BookMeta
from domain.model.book_detail import BookDetail

SCRAPE_HOST = "https://books.toscrape.com"
PAGE_URL_TEMPLATE = SCRAPE_HOST + "/catalogue/page-{}.html"
BOOK_URL_TEMPLATE = SCRAPE_HOST + "/catalogue/{}"

def responseOk(response: ApiResponse):
    return response.status_code == AppConst.HTTP_OK

# callback param calls from scraper, this would parse Book Meta html
def _mapBookMeta(element: BS) -> BookMeta:
    aTag = element.find("a")
    imgTag = element.find("img")
    href = aTag["href"] if aTag else ""
    title = imgTag.get("alt") if imgTag else ""
    return BookMeta(title=title, url=href)

# callback param calls from scraper, this would parse Book Details html
def _mapBook(element: BS) -> BookDetail:
    titleTag = element.find("h1")
    title = titleTag.text.strip() if titleTag else ""

    priceTag = element.select_one("p.price_color")
    price = priceTag.text.strip() if priceTag else ""
    return BookDetail(
        title=title,
        price=price
    )

# Book Scraping Implementation
class BookScrapeImp(IBookScrape):
    def __init__(self, scraper: IWebScarape, client: IHttpClient,):
        self.scraper = scraper
        self.client = client

    # This would fetach Book Meta from page (page have multiple books etails)
    async def _fetchPage(self, pageNumber: int):
        pageUrl = PAGE_URL_TEMPLATE.format(pageNumber)
        response = await self.client.get(pageUrl)

        if not responseOk(response):
            return []

        booksMetaList = self.scraper.getFromHtml(response.body, "article.product_pod", _mapBookMeta)

        bookScrapeTasks = []
        for bookMeta in booksMetaList:
            bookScrapeTasks.append(asyncio.create_task(self._fetchBook(bookMeta=bookMeta)))

        # this is a list of list
        bokResults = await asyncio.gather(*bookScrapeTasks)

        # flattening
        validBooks = list(filter(lambda b: b is not None, bokResults))

        return validBooks
    
    # This would fetach individual Book Details
    async def _fetchBook(self, bookMeta: BookMeta) -> BookDetail | None:
        bookUrl = BOOK_URL_TEMPLATE.format(bookMeta.url)
        response = await self.client.get(bookUrl)

        if not responseOk(response):
            return None
        
        bookDetail = self.scraper.getFromHtmlSingle(response.body, "article.product_page", _mapBook)
        await asyncio.sleep(random.uniform(0.1, 0.4))
        return bookDetail

    async def collectData(self, pageCount: int) -> List[BookDetail]:
        pageScrapeTasks = []
        for i in range(1, pageCount + 1):
            pageScrapeTasks.append(asyncio.create_task(self._fetchPage(i)))

        # list of list of books
        pagesResults = await asyncio.gather(*pageScrapeTasks)

        allBooks = list(chain.from_iterable(pagesResults))
        
        return allBooks


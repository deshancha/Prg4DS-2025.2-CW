import asyncio
import random
from typing import List
from itertools import chain
import re

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
    article = element.select_one("article.product_page")
    titleTag = element.find("h1")
    title = titleTag.text.strip() if titleTag else ""

    priceTag = article.select_one("p.price_color")
    price = priceTag.text.strip() if priceTag else ""

    availability_text = article.select_one("p.instock.availability").get_text(strip=True)
    available = "In stock" in availability_text
    stock_count = 0
    
    match = re.search(r"\((\d+)\s+available\)", availability_text)
    if match:
        stock_count = int(match.group(1))

    rating_tag = article.select_one("p.star-rating")
    rating = ""
    if rating_tag and rating_tag.get("class"):
        for c in rating_tag["class"]:
            if c != "star-rating":
                rating = c
                break

    desc_tag = article.select_one("#product_description ~ p")
    description = desc_tag.get_text(strip=True) if desc_tag else ""

    def get_table_value(label: str) -> str:
        row = article.select_one(f"table.table tr:has(th:-soup-contains('{label}')) td")
        return row.get_text(strip=True) if row else ""
    
    upc = get_table_value("UPC")
    product_type = get_table_value("Product Type")
    price_excl_tax = get_table_value("Price (excl. tax)")
    price_incl_tax = get_table_value("Price (incl. tax)")
    tax = get_table_value("Tax")
    num_reviews = int(get_table_value("Number of reviews") or 0)

    breadcrumb_items = element.select("ul.breadcrumb li a")  # note select() returns a list
    category = breadcrumb_items[-1].text.strip() if len(breadcrumb_items) >= 3 else ""  

    return BookDetail(
        title=title,
        price=price,
        category=category,
        available=available,
        stock_count=stock_count,
        rating=rating,
        description=description,
        upc=upc,
        product_type=product_type,
        price_excl_tax=price_excl_tax,
        price_incl_tax=price_incl_tax,
        tax=tax,
        num_reviews=num_reviews
    )

# Book Scraping Implementation
class BookScrapeImp(IBookScrape):
    def __init__(self, scraper: IWebScarape, client: IHttpClient,):
        self.scraper = scraper
        self.client = client

    # This would fetach Book Meta from page (page have multiple books etails)
    async def _fetchPage(self, pageNumber: int):
        pageUrl = PAGE_URL_TEMPLATE.format(pageNumber)
        await asyncio.sleep(random.uniform(1.5, 8.8))
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
        await asyncio.sleep(random.uniform(2.1, 5.6))
        bookUrl = BOOK_URL_TEMPLATE.format(bookMeta.url)
        response = await self.client.get(bookUrl)

        if not responseOk(response):
            return None
        
        bookDetail = self.scraper.getFromHtmlSingle(response.body, _mapBook)
        
        return bookDetail

    async def collectData(self, pageCount: int) -> List[BookDetail]:
        pageScrapeTasks = []
        for i in range(1, pageCount + 1):
            pageScrapeTasks.append(asyncio.create_task(self._fetchPage(i)))

        # list of list of books
        pagesResults = await asyncio.gather(*pageScrapeTasks)

        allBooks = list(chain.from_iterable(pagesResults))
        
        return allBooks


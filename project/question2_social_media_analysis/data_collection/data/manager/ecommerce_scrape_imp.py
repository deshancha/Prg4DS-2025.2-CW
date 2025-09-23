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
from domain.model.product_detail import ProductDetail
from domain.model.product_meta import ProductMeta

SCRAPE_HOST = "https://scrapeme.live/shop"
PAGE_URL_TEMPLATE = SCRAPE_HOST + "/page/{}/"

def responseOk(response: ApiResponse):
    return response.status_code == AppConst.HTTP_OK

# callback param calls from scraper, this would parse product Meta html
def _mapProductMeta(element: BS) -> ProductMeta:
    aTag = element.select_one("a.woocommerce-LoopProduct-link")
    titleTag = element.select_one("h2.woocommerce-loop-product__title")
    href = aTag["href"] if aTag else ""
    title = titleTag.text.strip() if titleTag else ""
    return ProductMeta(title=title, url=href)

# callback param calls from scraper, this would parse product Details html
def _mapProduct(element: BS) -> ProductDetail:
    titleTag = element.select_one("h1.product_title")
    title = titleTag.text.strip() if titleTag else ""

    priceTag = element.select_one("p.price")
    price = priceTag.text.strip() if priceTag else ""

    descTag = element.select_one("div.woocommerce-product-details__short-description p")
    description = descTag.text.strip() if descTag else ""

    stockTag = element.select_one("p.stock")
    stock = stockTag.text.strip() if stockTag else ""

    skuTag = element.select_one("span.sku")
    sku = skuTag.text.strip() if skuTag else ""

    categoryTags = element.select("span.posted_in a")
    categories = [cat.text.strip() for cat in categoryTags] if categoryTags else []

    tagTags = element.select("span.tagged_as a")
    tags = [t.text.strip() for t in tagTags] if tagTags else []

    return ProductDetail(
        title=title,
        price=price,
        description=description,
        stock=stock,
        sku=sku,
        categories=categories,
        tags=tags
    )

# ECommerce Scraping Implementation
class ECommerceScrapeImp(IBookScrape):
    def __init__(self, scraper: IWebScarape, client: IHttpClient,):
        self.scraper = scraper
        self.client = client

    # This would fetach Product Meta from page (page have multiple items details)
    async def _fetchPage(self, pageNumber: int):
        pageUrl = PAGE_URL_TEMPLATE.format(pageNumber)

        await asyncio.sleep(random.uniform(1.0, 3.0))
        
        response = await self.client.get(pageUrl)

        if not responseOk(response):
            return []

        # <ul class="products ..."> <li class="product ..."
        productMetaList = self.scraper.getFromHtml(response.body, "ul.products li.product", _mapProductMeta)

        productScrapeTasks = []
        for productMeta in productMetaList:
            productScrapeTasks.append(asyncio.create_task(self._fetchProduct(bookMeta=productMeta)))

        bokResults = await asyncio.gather(*productScrapeTasks)

        # flattening
        validProducts = list(filter(lambda b: b is not None, bokResults))

        return validProducts
    
    # This would fetach individual product Details
    async def _fetchProduct(self, bookMeta: ProductMeta) -> ProductDetail | None:
        await asyncio.sleep(random.uniform(0.2, 1.0))
        response = await self.client.get(bookMeta.url)

        if not responseOk(response):
            return None
        
        # <div id="primary" class="content-area">
        productDetail = self.scraper.getFromHtmlSingle(response.body, "div.content-area", _mapProduct)
        
        return productDetail

    async def collectData(self, pageCount: int) -> List[ProductDetail]:
        pageScrapeTasks = []
        for i in range(1, pageCount + 1):
            pageScrapeTasks.append(asyncio.create_task(self._fetchPage(i)))

        pagesResults = await asyncio.gather(*pageScrapeTasks)

        allBooks = list(chain.from_iterable(pagesResults))
        
        return allBooks
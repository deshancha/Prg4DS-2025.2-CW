import asyncio
from bs4 import BeautifulSoup as BS
from data.manager.http_client_imp import HttpClientImp
from domain.manager.ihhtp_client import IHttpClient
from domain.manager.iweb_scarpe import IWebScarape
from data.manager.web_scape_imp import WebScrapeImp
from domain.components.app_const import AppConst
from domain.model.product import Product
from domain.model.api_response import ApiResponse

SCRAPE_HOST = "https://books.toscrape.com"
PAGE_URL_TEMPLATE = SCRAPE_HOST + "/catalogue/page-{}.html"
BOOK_URL_TEMPLATE = SCRAPE_HOST + "/catalogue/{}"

# Helper for check Api Response is status code is 200
def responseOk(response: ApiResponse):
    return response.status_code == AppConst.HTTP_OK

# callback param calls from scraper, this would parse product html
def mapProduct(element: BS) -> Product:
    aTag = element.find("a")
    imgTag = element.find("img")
    href = aTag["href"] if aTag else ""
    title = imgTag.get("alt") if imgTag else ""
    return Product(title=title, url=href)

async def fetchPage(client: IHttpClient, pageNumber: int, scraper: IWebScarape):
    pageUrl = PAGE_URL_TEMPLATE.format(pageNumber)
    response = await client.get(pageUrl)

    if not responseOk(response):
        return []

    products = scraper.getFromHtml(response.body, "article.product_pod", mapProduct)
    for product in products:
        print(f"Page:{pageNumber} {product.title}")
    # TODO: Fetch books here
    return []

async def collect_data(fetchCount=1):
    client: IHttpClient = HttpClientImp(timeout=5)
    scraper: IWebScarape = WebScrapeImp()

    pageTasks = []
    for i in range(1, fetchCount + 1):
        pageTasks.append(asyncio.create_task(fetchPage(client, i, scraper)))

    booksList = await asyncio.gather(*pageTasks)

    print(f"Total: {len(booksList)}")
    
if __name__ == "__main__":
    asyncio.run(collect_data(fetchCount=2))


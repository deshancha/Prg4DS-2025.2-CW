
import os
import asyncio
from di.container import Container
from domain.usecases.collect_data_usecases import CollectDataUseCases
from util.docorators import measure_time

DATA_LOC = "files"
BOOKS_FILE = DATA_LOC + "/books.json"
PRODUCTS_FILE = DATA_LOC + "/products.json"
NEWS_FILE = DATA_LOC + "/news_rss.json"

# Dependancy Injection Container
container = Container()

@measure_time
async def booksScrape(collect_data_useCases:  CollectDataUseCases, pageCount: int):
    return await collect_data_useCases.booksScrape(pageCount)

@measure_time
async def eCommerceScrape(collect_data_useCases:  CollectDataUseCases, pageCount: int):
    return await collect_data_useCases.eCommerceScrape(pageCount)

@measure_time
async def rssScrape(collect_data_useCases:  CollectDataUseCases):
    return await collect_data_useCases.rssScrape()

""" collect and save books"""
async def collect_Books(fileName: str, fetchCount=1):
    collect_data_useCases = container.collect_data_useCases()
    save_data_useCases = container.save_data_useCases()

    booksList = await booksScrape(collect_data_useCases, pageCount=fetchCount)

    # for book in booksList:
    #     print(f"Title: {book.title}, Price: {book.price}\n======\n")

    print(f"Total Books: {len(booksList)}")

    await save_data_useCases.saveJson(booksList, fileName)

""" collect and save products from ecommerce"""
async def collect_products(fileName: str, fetchCount=1):
    collect_data_useCases = container.collect_data_useCases()
    save_data_useCases = container.save_data_useCases()

    productList = await eCommerceScrape(collect_data_useCases, pageCount=fetchCount)

    # for prodct in productList:
    #     print(f"Title: {prodct.title}, Price: {prodct.price}\n======\n")

    print(f"Total Products: {len(productList)}")

    await save_data_useCases.saveJson(productList, fileName)

""" collect and save rss feeds from news site"""
async def collect_rss(fileName: str):
    collect_data_useCases = container.collect_data_useCases()
    save_data_useCases = container.save_data_useCases()

    newsList = await rssScrape(collect_data_useCases)

    print(f"Total News Items: {len(newsList)}")

    await save_data_useCases.saveJson(newsList, fileName)
    
if __name__ == "__main__":
    os.makedirs("files", exist_ok=True)
    # one after another
    # asyncio.run(collect_Books(BOOKS_FILE, fetchCount=50))
    # asyncio.run(collect_products(PRODUCTS_FILE, fetchCount=5))
    asyncio.run(collect_rss(NEWS_FILE))


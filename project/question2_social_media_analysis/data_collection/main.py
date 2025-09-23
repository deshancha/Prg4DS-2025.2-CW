import asyncio
from di.container import Container
from domain.model.book_detail import BookDetail
from domain.usecases.collect_data_usecases import CollectDataUseCases
import time
import functools
from logger.logger import Logger 

DATA_LOC = "data"
BOOKS_FILE = DATA_LOC + "/books.json"
PRODUCTS_FILE = DATA_LOC + "/products.json"

def measure_time(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        end = time.time()
        Logger.info(f"took {end - start:.2f} seconds")
        return result
    return wrapper

@measure_time
async def booksScrape(collect_data_useCases:  CollectDataUseCases, pageCount: int):
    return await collect_data_useCases.booksScrape(pageCount)

async def collect_data(fetchCount=1):
    container = Container()
    collect_data_useCases = container.collect_data_useCases()
    save_data_useCases = container.save_data_useCases()

    booksList = await booksScrape(collect_data_useCases, pageCount=fetchCount)
    # productList = await collect_data_useCases.eCommerceScrape(pageCount=fetchCount)

    # for book in booksList:
    #     print(f"Title: {book.title}, Price: {book.price}\n======\n")

    # for prodct in productList:
    #     print(f"Title: {prodct.title}, Price: {prodct.price}\n======\n")

    # print(f"Total: {len(productList)}")
    print(f"Total: {len(booksList)}")

    await save_data_useCases.saveJson(booksList, BOOKS_FILE)
    
if __name__ == "__main__":
    asyncio.run(collect_data(fetchCount=50))


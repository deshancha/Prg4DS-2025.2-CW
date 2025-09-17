import asyncio
from di.container import Container
from domain.model.book_detail import BookDetail

async def collect_data(fetchCount=1):
    container = Container()
    useCases = container.useCases()

    # booksList = await useCases.booksScrape(pageCount=fetchCount)
    productList = await useCases.eCommerceScrape(pageCount=fetchCount)

    # for book in booksList:
    #     print(f"Title: {book.title}, Price: {book.price}\n======\n")

    for prodct in productList:
        print(f"Title: {prodct.title}, Price: {prodct.price}\n======\n")

    print(f"Total: {len(productList)}")
    
if __name__ == "__main__":
    asyncio.run(collect_data(fetchCount=1))


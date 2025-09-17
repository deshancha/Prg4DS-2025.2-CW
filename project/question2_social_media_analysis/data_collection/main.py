import asyncio
from di.container import Container
from domain.model.book_detail import BookDetail

async def collect_data(fetchCount=1):
    container = Container()
    useCases = container.useCases()

    booksList = await useCases.booksScrape(pageCount=fetchCount)

    for book in booksList:
        print(f"Title: {book.title}, Price: {book.price}\n======\n")

    print(f"Total: {len(booksList)}")
    
if __name__ == "__main__":
    asyncio.run(collect_data(fetchCount=2))


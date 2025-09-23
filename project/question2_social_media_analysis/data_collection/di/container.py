from dependency_injector import containers, providers
from domain.manager.ihhtp_client import IHttpClient
from data.manager.http_client_imp import HttpClientImp
from domain.manager.iweb_scarpe import IWebScarape
from data.manager.web_scape_imp import WebScrapeImp
from data.manager.book_scrape_imp import BookScrapeImp
from domain.manager.ibook_scrape import IBookScrape
from domain.manager.iecommerce_scrape import IECommerceScrape
from data.manager.ecommerce_scrape_imp import ECommerceScrapeImp
from domain.manager.isave_file import ISaveFile
from data.manager.save_file_imp import SaveFileImp
from domain.usecases.collect_data_usecases import CollectDataUseCases
from domain.usecases.save_data_usecases import SaveDataUseCases


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    httpClient: providers.Provider[IHttpClient] = providers.Singleton(
        HttpClientImp,
        timeout=3
    )

    save_data: providers.Provider[ISaveFile] = providers.Singleton(
        SaveFileImp
    )

    webScraper: providers.Provider[IWebScarape] = providers.Singleton(
        WebScrapeImp
    )

    bookScraper: providers.Provider[IBookScrape] = providers.Factory(
        BookScrapeImp,
        client=httpClient,
        scraper=webScraper
    )

    ecommerceScraper: providers.Provider[IECommerceScrape] = providers.Factory(
        ECommerceScrapeImp,
        client=httpClient,
        scraper=webScraper
    )

    collect_data_useCases = providers.Factory(
        CollectDataUseCases,
        iBookScrape=bookScraper,
        iEcommerceScrape=ecommerceScraper
    )

    save_data_useCases = providers.Factory(
        SaveDataUseCases,
        isaveFile=save_data
    )
import asyncio
import random
from typing import List
from itertools import chain

from bs4 import BeautifulSoup as BS
from domain.manager.ihhtp_client import IHttpClient
from domain.manager.iweb_scarpe import IWebScarape
from domain.manager.irss_xml_scrape import IRSSXMLScrape
from domain.components.app_const import AppConst
from domain.model.api_response import ApiResponse
from domain.model.product_detail import ProductDetail
from domain.model.rss_element import RSSElement

RSS_HOST = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"

def responseOk(response: ApiResponse):
    return response.status_code == AppConst.HTTP_OK

# callback param calls from scraper, this would parse product Details html
def _mapItem(element) -> RSSElement:
    title = element.find("title").text if element.find("title") else ""
    link = element.find("link").text if element.find("link") else ""
    description = element.find("description").text if element.find("description") else ""
    pubDate = element.find("pubDate").text if element.find("pubDate") else ""
    
    return RSSElement(
        title=title,
        link=link,
        description=description,
        pubDate=pubDate
    )

# XML Scraping Implementation
class RSSXMLScareImp(IRSSXMLScrape):
    def __init__(self, scraper: IWebScarape, client: IHttpClient,):
        self.scraper = scraper
        self.client = client

    async def collectData(self) -> List[RSSElement]:
        response = await self.client.get(RSS_HOST)

        if not responseOk(response):
            return []
        
        newsElements = self.scraper.getFromXml(response.body, "item", _mapItem)
        
        return newsElements
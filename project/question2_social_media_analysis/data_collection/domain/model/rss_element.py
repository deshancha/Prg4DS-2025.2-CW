from dataclasses import dataclass

@dataclass
class RSSElement:
    title: str
    link: str
    description: str
    pubDate: str
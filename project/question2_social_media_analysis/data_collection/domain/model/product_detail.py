from dataclasses import dataclass

@dataclass
class ProductDetail:
    title: str
    price: str
    description: str
    stock: str
    sku: str
    categories: list[str]
    tags: list[str]
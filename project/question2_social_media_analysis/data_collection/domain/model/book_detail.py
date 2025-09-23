from dataclasses import dataclass

@dataclass
class BookDetail:
    title: str
    price: str
    available: bool
    stock_count: int
    rating: str
    description: str
    upc: str
    product_type: str
    price_excl_tax: str
    price_incl_tax: str
    tax: str
    num_reviews: int
    

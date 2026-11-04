from fastapi import FastAPI
from src.models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to My Shop..."


products = [
    Product(1, "phone", "budget phone", 99, 10),
    Product(2, "laptop", "gaming laptop", 999, 5),
    Product(3, "tablet", "10-inch tablet", 299, 8),
    Product(4, "headphones", "noise cancelling headphones", 149, 15),
    Product(5, "smartwatch", "fitness smartwatch", 199, 12),
    Product(6, "keyboard", "mechanical keyboard", 79, 20),
    Product(7, "mouse", "wireless mouse", 29, 25),
    Product(8, "monitor", "27-inch 4K monitor", 349, 6),
    Product(9, "speaker", "bluetooth speaker", 59, 18),
    Product(10, "camera", "mirrorless camera", 799, 4),
]

@app.get("/products")
def get_all_products():
    return products
from fastapi import FastAPI
from src.models import Product, UpdateProduct
from src.validation_handler import register_exception_handlers


app = FastAPI()
register_exception_handlers(app)

@app.get("/")
def greet():
    return "Welcome to My Shop..."


products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    Product(id=2, name="laptop", description="gaming laptop", price=999, quantity=5),
    Product(id=3, name="tablet", description="10-inch tablet", price=299, quantity=8),
    Product(id=4, name="headphones", description="noise cancelling headphones", price=149, quantity=15),
    Product(id=5, name="smartwatch", description="fitness smartwatch", price=199, quantity=12),
    Product(id=6, name="keyboard", description="mechanical keyboard", price=79, quantity=20),
    Product(id=7, name="mouse", description="wireless mouse", price=29, quantity=25),
    Product(id=8, name="monitor", description="27-inch 4K monitor", price=349, quantity=6),
    Product(id=9, name="speaker", description="bluetooth speaker", price=59, quantity=18),
    Product(id=10, name="camera", description="mirrorless camera", price=799, quantity=4),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
    return f"Product not found..."


@app.post("/product")
def add_product(product:Product):
    products.append(product)
    return product

@app.put("/product/{id}")
def update_product(id:int, product:UpdateProduct):
    for index, existing in enumerate(products):
        if existing.id == id:
            updated = existing.model_copy(update=product.model_dump())
            products[index] = updated
            return "Product updated successfully..."

    return "Product not found..."


@app.patch("/product/{id}")
def update_product(id:int, product:UpdateProduct):
    for index, existing in enumerate(products):
        if existing.id == id:
            updated = existing.model_copy(update=product.model_dump(exclude_unset=True))
            products[index] = updated
            return "Product updated successfully..."

    return "Product not found..."


@app.delete("/product/{id}")
def delete_product_by_id(id:int):
    for index, product in enumerate(products):
        if product.id == id:
            del products[index]
            return "Product deleted..."
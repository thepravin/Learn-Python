from fastapi import FastAPI
from src.models import Product, UpdateProduct, ProductCreate
from src.validation_handler import register_exception_handlers
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends
from db.connection import get_db
from db.db_models import Product as ProductDB

app = FastAPI()
register_exception_handlers(app)
DbSession = Annotated[Session, Depends(get_db)]

@app.get("/")
def greet():
    return "Welcome to My Shop..."


products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10)
]

@app.get("/products", response_model=list[Product])
def get_all_products(db:DbSession):
    stmt = select(ProductDB).order_by(ProductDB.id).limit(12).offset(0)
    return db.scalars(stmt).all()

@app.get("/product/{id}")
def get_product_by_id(id:int, db:DbSession):
    product = db.scalar(select(ProductDB).where(ProductDB.id == id))
    if product:
        return product
    return f"Product not found..."


@app.post("/product", response_model=Product)
def add_product(product:ProductCreate, db:DbSession):
    new_product = ProductDB(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

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
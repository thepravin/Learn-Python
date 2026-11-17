from fastapi import FastAPI, status, HTTPException
from src.models import Product, UpdateProduct, ProductCreate, ProductPatch
from src.validation_handler import register_exception_handlers
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from fastapi import Depends
from db.connection import get_db
from db.db_models import Product as ProductDB
from fastapi.responses import JSONResponse

app = FastAPI()
register_exception_handlers(app)
DbSession = Annotated[Session, Depends(get_db)]

@app.get("/")
def greet():
    return "Welcome to My Shop..."


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

def get_product_or_404(db: Session, id: int) -> ProductDB:
    product = db.get(ProductDB, id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product {id} not found")
    return product


def save_product_changes(db: Session, product: ProductDB, changes: dict) -> ProductDB:
    for field, value in changes.items():
        setattr(product, field, value)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Product could not be updated")

    db.refresh(product)
    return product


@app.put("/product/{id}", response_model=Product, status_code=status.HTTP_200_OK)
def replace_product(id: int, product: UpdateProduct, db: DbSession):
    existing = get_product_or_404(db, id)
    return save_product_changes(db, existing, product.model_dump())


@app.patch("/product/{id}", response_model=Product, status_code=status.HTTP_200_OK)
def patch_product(id: int, product: ProductPatch, db: DbSession):
    existing = get_product_or_404(db, id)
    return save_product_changes(db, existing, product.model_dump(exclude_unset=True))


@app.delete("/product/{id}")
def delete_product_by_id(id:int, db:DbSession):
    product = db.get(ProductDB, id)
    if product is None:
        return JSONResponse(
            status_code=404,
            content={
                "success":False,
                "message":"Product not available"
            }
        )
    
    db.delete(product)
    db.commit()
    return JSONResponse(
        status_code=200,
        content={
            "success":True,
            "message":"Product deleted",
            "id":id
        }
    )
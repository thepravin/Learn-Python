from sqlalchemy.orm import Session
from src.models import UpdateProduct
from db.db_models import Product as db_model_product
from db.connection import SessionLocal


SEED_PRODUCTS  = [
    UpdateProduct(name="phone", description="budget phone", price=99, quantity=10),
    UpdateProduct(name="laptop", description="gaming laptop", price=999, quantity=5),
    UpdateProduct(name="tablet", description="10-inch tablet", price=299, quantity=8),
    UpdateProduct(name="headphones", description="noise cancelling headphones", price=149, quantity=15),
    UpdateProduct(name="smartwatch", description="fitness smartwatch", price=199, quantity=12),
    UpdateProduct(name="keyboard", description="mechanical keyboard", price=79, quantity=20),
    UpdateProduct(name="mouse", description="wireless mouse", price=29, quantity=25),
    UpdateProduct(name="monitor", description="27-inch 4K monitor", price=349, quantity=6),
    UpdateProduct(name="speaker", description="bluetooth speaker", price=59, quantity=18),
    UpdateProduct(name="camera", description="mirrorless camera", price=799, quantity=4),
]

def seed_products(db: Session):
    for product in SEED_PRODUCTS:
        db.add(db_model_product(**product.model_dump()))
    db.commit()

def main():
    with SessionLocal() as session:
        seed_products(session)


if __name__ == "__main__":
    main()
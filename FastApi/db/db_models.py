from sqlalchemy import Integer, String, Numeric, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from decimal import Decimal

class Base(DeclarativeBase):
    pass

class Product(Base):

    __tablename__ = "products"

    __table_args__ = (
        CheckConstraint("price > 0", name="ck_products_price_positive"),
        CheckConstraint("quantity >= 0", name="ck_products_quantity_non_negative"),
    )

    id: Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100))
    description:Mapped[str]=mapped_column(String(250))
    price:Mapped[Decimal]=mapped_column(Numeric(10,2))
    quantity:Mapped[int]=mapped_column(Integer)
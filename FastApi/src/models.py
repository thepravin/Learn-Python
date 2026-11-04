from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str = Field(max_length=500)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)

class UpdateProduct(ProductBase):
    pass

class Product(ProductBase):
    id: int
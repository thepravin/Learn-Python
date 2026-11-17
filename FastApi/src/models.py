from pydantic import BaseModel, Field, ConfigDict, field_validator

class ProductBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str = Field(max_length=500)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)

class UpdateProduct(ProductBase):
    pass

class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int

class ProductCreate(ProductBase):
    pass

class ProductPatch(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    price: float | None = Field(default=None, gt=0)
    quantity: int | None = Field(default=None, ge=0)

    @field_validator("*", mode="before")
    @classmethod
    def reject_null(cls, value):
        if value is None:
            raise ValueError("Field cannot be null")
        return value
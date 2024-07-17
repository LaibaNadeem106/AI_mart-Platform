from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    price: float
    expiry: Optional[str] = None
    brand: Optional[str] = None
    weight: Optional[float] = None
    category: str  # This shall be pre-defined by Platform
    sku: Optional[str] = None
    rating: List["ProductRating"] = Relationship(back_populates="product")

class ProductRating(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id")
    rating: int
    review: Optional[str] = None
    product: "Product" = Relationship(back_populates="rating")

class ProductUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    expiry: Optional[str] = None
    brand: Optional[str] = None
    weight: Optional[float] = None
    category: Optional[str] = None
    sku: Optional[str] = None

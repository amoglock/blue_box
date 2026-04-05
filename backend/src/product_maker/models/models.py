from typing import Optional

from sqlmodel import SQLModel


class PortionProduct(SQLModel):
    department: str
    title: str
    ingredients: dict[str, float]
    recipe: str


class Product(SQLModel):
    group: str
    net_weight: float
    description: Optional[str] = None

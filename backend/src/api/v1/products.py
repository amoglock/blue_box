from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.database import get_db
from ...core.product_maker import ProductService


router = APIRouter(prefix="/api/v1/products", tags=["products"])


class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int


@router.get("/")
async def get_products(
        skip: int = 0,
        limit: int = 100,
        db: AsyncSession = Depends(get_db),
) -> dict[str, Any]:
    service = ProductService(db)
    products = await service.get_products(skip=skip, limit=limit)
    return {"data": products, "total": len(products)}


@router.post("/")
async def create_product(
        product: ProductCreate,
        db: AsyncSession = Depends(get_db),
):
    service = ProductService(db)
    return await service.create_product(product.model_dump())


@router.get("/{product_id}")
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    service = ProductService(db)
    product = await service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

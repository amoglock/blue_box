from typing import Annotated

from fastapi import APIRouter, Depends

from src.product_maker.models.models import Product
from src.product_maker.service.product_service import ProductService

product_router = APIRouter(
    prefix='/products',
    tags=['products'],
)


@product_router.get('')
async def get_product():
    return {"data": "some data"}


@product_router.post('/create_product')
async def create_product(
        product_service: Annotated[ProductService, Depends()],
        new_product: Product,

):
    return {new_product.title: new_product.ingredients}

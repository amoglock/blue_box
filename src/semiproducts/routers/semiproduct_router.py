from typing import Annotated
from fastapi import APIRouter, Depends

from src.semiproducts.models.models import Semiproduct
from src.semiproducts.service.semiproducts_service import SemiproductService


semiproduct_router = APIRouter(
    prefix='/semiproducts',
    tags=['semiproducts'],
)

@semiproduct_router.post('/add')
async def create_semiproduct(
    semiproduct: Semiproduct,
    semiproduct_service: Annotated[SemiproductService, Depends()],
):
    return await semiproduct_service.create_semiproduct(semiproduct)
    
    

@semiproduct_router.get('')
async def get_all(
    semiproduct_service: Annotated[SemiproductService, Depends()],
):
    return await semiproduct_service.get_all()
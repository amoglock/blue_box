from sqlmodel import select
from src.raw_storage.models.models import ResponseModel
from src.semiproducts.repository.semiproduct_repository import SemiproductRepository


class SemiproductService:
    """
    """
    def __init__(self):
        self.semiproduct_repository = SemiproductRepository()
        self.response = ResponseModel()

    async def get_all(self) -> ResponseModel:
        semiproducts = await self.semiproduct_repository.get_all_semiproducts()
        print(semiproducts)
        self.response.data = semiproducts
        return self.response
    
    async def create_semiproduct(self, semiproduct):

        return await self.semiproduct_repository.create_semiproduct(semiproduct)
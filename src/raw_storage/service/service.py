from typing import Annotated

from fastapi import Depends

from src.raw_storage.models.models import IncomingRaw
from src.raw_storage.models.response_models import ResponseModel
from src.raw_storage.repository.repository import RawRepository


class RawStorageService:
    def __init__(self):
        self.raw_repository = RawRepository()
        self.response = ResponseModel()

    # async def arrival_raw(self, raw: IncomingRaw):
    #     return await self.raw_repository.add_raw(raw)

    async def get_storage(self, name):
        self.response.data = await self.raw_repository.get_storage(name)

        if name and not self.response.data:
            self.response.status = False
            self.response.message = f"Item {name} not found"
            return self.response

        return self.response

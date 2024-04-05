from typing import Annotated

from fastapi import Depends

from src.raw_storage.models.models import IncomingRaw, RawResponse
from src.raw_storage.models.response_models import ResponseModel
from src.raw_storage.repository.repository import RawRepository


class RawStorageService:
    def __init__(self):
        self.raw_repository = RawRepository()
        self.response = ResponseModel()

    async def arrival_raw(self, raw: IncomingRaw):
        self.response.data = await self.raw_repository.add_raw(raw)
        self.response.message = f"Item {raw.title} in amount {raw.incoming_amount} added successful"
        return self.response

    async def get_storage(self, name):
        item_from_base = await self.raw_repository.get_storage(name)
        self.response.data = RawResponse(**item_from_base[name].model_dump())

        if name and not self.response.data:
            self.response.status = False
            self.response.message = f"Item {name} not found"
            return self.response

        return self.response

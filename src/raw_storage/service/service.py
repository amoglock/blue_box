from sqlalchemy.orm import Session

from src.raw_storage.models.models import IncomingRaw, RawResponse
from src.raw_storage.models.response_models import ResponseModel
from src.raw_storage.repository.repository import RawRepository


class RawStorageService:
    def __init__(self):
        self.raw_repository = RawRepository()
        self.response = ResponseModel()

    async def arrival_raw(self, db: Session, raw: IncomingRaw):
        self.response.data = await self.raw_repository.add_raw(db, raw)
        self.response.message = f"Item {raw.title} in amount {raw.incoming_amount} added successful"
        return self.response

    async def get_storage(self, name):
        item_from_base = await self.raw_repository.get_storage(name)

        if name and not item_from_base:
            self.response.status = False
            self.response.message = f"Item {name} not found"
            return self.response

        if name:
            self.response.data = RawResponse(**item_from_base.model_dump())
            return self.response

        self.response.data = item_from_base
        return self.response

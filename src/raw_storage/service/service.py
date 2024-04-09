from src.raw_storage.models.models import IncomingRaw, RawResponse, ResponseModel, Raw
from src.raw_storage.repository.repository import RawRepository


class RawStorageService:
    def __init__(self):
        self.raw_repository = RawRepository()
        self.response = ResponseModel()

    async def arrival_raw(self, raw: IncomingRaw):
        incoming_raw = Raw.model_validate(raw)
        await self.raw_repository.add_raw(incoming_raw)

        self.response.data = raw
        self.response.message = f"Item {raw.title} in amount {raw.incoming_amount} added successful"

        return self.response

    async def get_storage(self, name):
        item_from_base = await self.raw_repository.get_storage(name)

        if name and not item_from_base:
            self.response.status = False
            self.response.message = f"Item {name} not found"
            return self.response

        if name:
            self.response.data = item_from_base
            return self.response

        self.response.message = "No item for search"
        self.response.data = item_from_base
        return self.response

from fastapi import Depends

from src.raw_storage.models.models import IncomingRaw
from src.raw_storage.repository.repository import RawRepository


class RawStorageService:
    def __init__(self, raw_repository: RawRepository = Depends()):
        self.raw_repository = raw_repository

    # async def arrival_raw(self, raw: IncomingRaw):
    #     return await self.raw_repository.add_raw(raw)

    async def get_storage(self, name):
        result = await self.raw_repository.get_storage(name)
        if name and not result:
            return {"data": f"Item {name} not found", "result": result}
        return {"data": "success", "result": result}

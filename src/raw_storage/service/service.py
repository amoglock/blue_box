from fastapi import Depends

from src.raw_storage.models.models import Raw
from src.raw_storage.repository.repository import RawRepository


class RawStorageService:
    def __init__(self, raw_repository: RawRepository = Depends()):
        self.raw_repository = raw_repository

    async def arrival_raw(self, raw: Raw):
        return await self.raw_repository.add_raw(raw)

    async def get_storage(self, name=None):
        return await self.raw_repository.get_storage(name)

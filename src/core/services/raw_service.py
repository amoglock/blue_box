from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.crud.raw_crud import RawCrud
from src.core.schemas import CreateRaw
from src.database.models import Raw


class RawService:

    def __init__(self, raw_crud: RawCrud = Depends()):
        self.raw_crud = raw_crud

    async def post_raw(self, raw_in: CreateRaw) -> Raw:
        return await self.raw_crud.post_raw(raw_in=raw_in)


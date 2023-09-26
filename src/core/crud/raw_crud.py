from fastapi import Depends
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.schemas import CreateRaw
from src.database import db_helper
from src.database.models import Raw


class RawCrud:

    def __init__(self, session: AsyncSession = Depends(db_helper.scope_session_dependency)):
        self.session = session

    async def post_raw(self, raw_in: CreateRaw) -> Raw:
        raw = Raw(**raw_in.model_dump())
        self.session.add(raw)
        await self.session.commit()
        return raw

    async def get_raw_list(self):
        stmt = select(Raw).order_by(Raw.id)
        result: Result = await self.session.execute(stmt)
        raw = result.scalars().all()
        return list(raw)

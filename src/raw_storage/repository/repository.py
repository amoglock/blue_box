from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from src.database import SessionLocal
from src.raw_storage.models.models import IncomingRaw, IncomingRawDB


class RawRepository:

    @staticmethod
    async def add_raw(db: Session, raw: IncomingRaw,) -> IncomingRaw:
        db.add(raw)
        db.commit()

        return raw

    async def get_storage(self, name):
        """

        :param name:
        :return:
        """
        if name:
            return self.storage.get(name)
        return self.storage

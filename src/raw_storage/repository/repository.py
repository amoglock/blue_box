from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from src.database import engine, Raw
from src.raw_storage.models.models import IncomingRaw
from sqlmodel import Session


class RawRepository:

    @staticmethod
    async def add_raw(incoming_raw: Raw) -> Raw:
        with Session(engine) as session:
            session.add(incoming_raw)
            session.commit()

        return incoming_raw

    async def get_storage(self, name):
        """

        :param name:
        :return:
        """
        if name:
            return self.storage.get(name)
        return self.storage

from sqlmodel import Session, select

from src.database import engine

from src.raw_storage.models.models import Raw


class RawRepository:

    @staticmethod
    async def add_raw(incoming_raw: Raw) -> None:
        with Session(engine) as session:
            session.add(incoming_raw)
            session.commit()

    async def get_storage(self, name):
        """

        :param name:
        :return:
        """
        if name:
            with Session(engine) as session:
                statement = select(Raw).where(Raw.title == name)
                result = session.exec(statement).first()
                return result
        return {"data": "no data"}

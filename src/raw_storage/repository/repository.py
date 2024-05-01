from sqlmodel import Session, select

from src.database import engine

from src.raw_storage.models.models import Raw


class RawRepository:
    def __init__(self):
        self.engine = engine

    async def add_raw(self, incoming_raw: Raw) -> None:
        """

        :param incoming_raw:
        :return:
        """
        with Session(self.engine) as session:
            session.add(incoming_raw)
            session.commit()

    async def get_storage(self, name) -> Raw | dict[str, str]:
        """

        :param name:
        :return:
        """
        if name:
            with Session(self.engine) as session:
                statement = select(Raw).where(Raw.title == name)
                result = session.exec(statement).first()
            return result
        return {"data": "no data"}

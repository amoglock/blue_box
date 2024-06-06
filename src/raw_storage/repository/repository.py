from sqlmodel import Session, select

from src.database import engine

from src.raw_storage.models.models import Raw


class RawRepository:
    def __init__(self):
        self.engine = engine

    async def add_raw(self, incoming_raw: Raw) -> None:
        """

        :param incoming_raw:
        :return: None
        """
        with Session(self.engine) as session:
            session.add(incoming_raw)
            session.commit()

    async def get_storage(self, name: str, group: Raw) -> Raw | dict[str, str]:
        """

        :param group:
        :param name:
        :return:
        """
        if name:
            with Session(self.engine) as session:
                statement = select(group).where(group.title == name)
                result = session.exec(statement).first()
            return result
        return {"data": "no data"}

    async def delivery_raw(self, name: str, amount: int | float):
        """

        :param name:
        :param amount:
        :return:
        """

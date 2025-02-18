from sqlalchemy import literal
from sqlmodel import Session, select, union_all

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

    async def get_all_storage(self) -> dict:
        """
        """
        with Session(self.engine) as session:
            raw_subclasses = Raw.__subclasses__()
            result = {}
            
            for model in raw_subclasses:
                statement = select(model)
                records = session.exec(statement).all()
                result[model.__name__] = records
                
            return result       

    async def get_storage(self, name: str, group: Raw) -> Raw | dict[str, str]:
        """

        :param group:
        :param name:
        :return:
        """

        with Session(self.engine) as session:
            statement = select(group).where(group.title == name)
            result = session.exec(statement).first()
        return result

    async def delivery_raw(self, name: str, amount: float):
        """

        :param name:
        :param amount:
        :return:
        """
        ...


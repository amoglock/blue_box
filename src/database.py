from datetime import date

from sqlmodel import Field, SQLModel, create_engine


class Raw(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    title: str
    group: str
    supplier: str
    is_frozen: bool
    delivery_date: date
    production_date: date
    expiration_date: date


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

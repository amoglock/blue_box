import uuid

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


def generate_uuid():
    return str(uuid.uuid4())


class Base(DeclarativeBase):
    __abstract__ = True

    @classmethod
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[str] = mapped_column(primary_key=True, default=generate_uuid)

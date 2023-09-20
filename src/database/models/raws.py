from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class Raw(Base):
    name: Mapped[str] = mapped_column(unique=True)
    supplier: Mapped[str]
    amount: Mapped[float]

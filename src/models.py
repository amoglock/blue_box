from sqlalchemy import Column, Integer, String, Boolean, Date
from src.database import Base


class Raw(Base):
    __tablename__ = "raw_storage"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    group = Column(String)
    supplier = Column(String)
    incoming_amount = Column(Integer)
    is_frozen = Column(Boolean)
    delivery_date = Column(Date)
    production_date = Column(Date)
    expiration_date = Column(Date)

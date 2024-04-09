from datetime import date

from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class Raw(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    title: str
    group: str
    supplier: str
    is_frozen: bool
    delivery_date: date
    production_date: date
    expiration_date: date


class RawResponse(SQLModel):
    title: str = Field(description="Name of raw")
    group: str
    supplier: str = Field(description="Name of supplier")


class IncomingRaw(RawResponse):
    incoming_amount: float | int
    is_frozen: bool = Field(default=False)
    delivery_date: date = Field(default_factory=date.today)
    production_date: date | None = None
    expiration_date: date | None = None


class ResponseModel(BaseModel):
    status: bool = Field(default=True)
    message: str | None = "success"
    data: IncomingRaw | dict = {}

from datetime import date

from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class Raw(SQLModel):
    id: int | None = Field(primary_key=True, default=None)
    title: str
    supplier: str
    incoming_amount: float
    is_frozen: bool
    delivery_date: date
    production_date: date
    expiration_date: date

class RawResponse(SQLModel):
    title: str = Field(description="Name of raw", nullable=False, index=True)
    group: str = Field(description="Group name of raw type", nullable=False)
    supplier: str = Field(description="Name of supplier", nullable=False, index=True)


class IncomingRaw(RawResponse):
    incoming_amount: float | int = Field(description="Amount incoming raw")
    is_frozen: bool = Field(default=False)
    delivery_date: date = Field(default_factory=date.today)
    production_date: date | None = None
    expiration_date: date | None = None


class ResponseModel(BaseModel):
    status: bool = Field(default=True)
    message: str | None = "success"
    data: Raw | None = None

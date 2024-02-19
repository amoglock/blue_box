from datetime import date, datetime

from pydantic import BaseModel, Field, field_validator


class RawResponse(BaseModel):
    title: str = Field(description="Name of raw", examples=["Dragon Fruit"])
    group: str
    supplier: str = Field(description="Name of supplier", examples=["Microsoft"])


class IncomingRaw(RawResponse):
    incoming_amount: float | int
    delivery_date: date = Field(default_factory=date.today)
    production_date: date | None = None
    expiration_date: date | None = None

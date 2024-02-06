from datetime import date, datetime

from pydantic import BaseModel, Field, field_validator


class RawResponse(BaseModel):
    title: str = Field(description="Name of raw", examples=["Dragon Fruit"])
    supplier: str = Field(description="Name of supplier", examples=["Microsoft"])


class Raw(RawResponse):
    amount: float = Field()
    delivery_date: date

    # @field_validator("delivery_date")
    # @classmethod
    # def parse_delivery_date(cls, value: str):
    #     print(type(value))
    #     if isinstance(value, str):
    #         try:
    #             return datetime.strptime(value, "%d.%m.%Y").date()
    #         except ValueError:
    #             raise ValueError("Date format is incorrect. Use DD.MM.YYYY")

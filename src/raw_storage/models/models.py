from enum import Enum

from pydantic import BaseModel, Field


class RawResponse(BaseModel):
    title: str = Field(description="Name of raw", examples=["Dragon Fruit"])
    supplier: str = Field(description="Name of supplier", examples=["Microsoft"])


class Raw(RawResponse):
    amount: float = Field()

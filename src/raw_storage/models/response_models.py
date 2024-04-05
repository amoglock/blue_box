from typing import Union

from pydantic import BaseModel, Field

from src.raw_storage.models.models import IncomingRaw, RawResponse


class ResponseModel(BaseModel):
    status: bool = Field(default=True)
    message: str | None = "success"
    data: RawResponse | dict = {}

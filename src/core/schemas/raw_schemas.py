from pydantic import BaseModel


class CreateRaw(BaseModel):
    name: str
    supplier: str
    amount: float


class Raw(CreateRaw):
    id: str

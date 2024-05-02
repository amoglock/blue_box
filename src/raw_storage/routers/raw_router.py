from enum import Enum
from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlmodel import SQLModel

from src.raw_storage.service.service import RawStorageService
from src.raw_storage.models.models import IncomingRaw, ResponseModel, Vegetables, Meat, Gastronomy

raw_router = APIRouter(
    prefix='/raw',
    tags=['raw'],
)


class Groups(str, Enum):
    vegetables = "Vegetables"
    meat = "Meat"
    gastronomy = "Gastronomy"


@raw_router.post("/arrival",
                 response_model=ResponseModel,
                 response_model_exclude={"data": "id"},
                 description="Add raw element into the base",
                 )
async def arrival_raw(
        raw_storage_service: Annotated[RawStorageService, Depends()],
        raw: IncomingRaw,
):
    return await raw_storage_service.arrival_raw(raw)


@raw_router.get("/get_storage",
                response_model=ResponseModel,
                response_model_exclude={"data": "id"},
                description="Get a raw from the base",
                )
async def get_storage(
        raw_storage_service: Annotated[RawStorageService, Depends()],
        group: Groups,
        name: Annotated[
            str | None,
            Query(
                title="Query string",
                description="Query string for searching for an item in the database by its name",
            ),] = None,
):
    return await raw_storage_service.get_storage(name, group)

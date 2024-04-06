from typing import Annotated

from fastapi import APIRouter, Depends, Query

from src.raw_storage.models.response_models import ResponseModel
from src.raw_storage.service.service import RawStorageService
from src.raw_storage.models.models import IncomingRaw

raw_router = APIRouter(
    prefix='/raw',
    tags=['raw'],
)


@raw_router.post("/arrival", response_model=ResponseModel)
async def arrival_raw(
        raw_storage_service: Annotated[RawStorageService, Depends()],
        raw: IncomingRaw,
):
    return await raw_storage_service.arrival_raw(raw)


@raw_router.get("/get_storage", response_model=ResponseModel)
async def get_storage(
        raw_storage_service: Annotated[RawStorageService, Depends()],
        name: Annotated[
            str | None,
            Query(
                title="Query string",
                description="Query string for searching for an item in the database by its name",
            ),] = None,
):
    return await raw_storage_service.get_storage(name)

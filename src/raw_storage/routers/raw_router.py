from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query

from src.raw_storage.service.service import RawStorageService
from src.raw_storage.models.models import RawResponse, IncomingRaw


raw_router = APIRouter(
    prefix='/raw',
    tags=['raw'],
)


@raw_router.post("/arrival")
async def arrival_raw(
        raw: IncomingRaw,
        raw_storage_service: RawStorageService = Depends(),
                      ):
    return await raw_storage_service.arrival_raw(raw)


@raw_router.get("/get_storage")
async def get_storage(
        raw_storage_service: RawStorageService = Depends(),
        name: Annotated[str | None, Query()] = None,
):
    if name:
        return await raw_storage_service.get_storage(name)
    return await raw_storage_service.get_storage()

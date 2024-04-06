from datetime import date
from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session

from src.database import get_db
from src.raw_storage.models.response_models import ResponseModel
from src.raw_storage.service.service import RawStorageService
from src.raw_storage.models.models import RawResponse, IncomingRaw

raw_router = APIRouter(
    prefix='/raw',
    tags=['raw'],
)


@raw_router.post("/arrival", response_model=ResponseModel)
async def arrival_raw(
        db: Annotated[Session, Depends(get_db)],
        raw_storage_service: Annotated[RawStorageService, Depends()],
        raw: IncomingRaw,
):
    return await raw_storage_service.arrival_raw(db, raw)


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

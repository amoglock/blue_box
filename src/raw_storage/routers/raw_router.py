from fastapi import APIRouter

from src.raw_storage.models.models import RawResponse, Raw
raw_router = APIRouter(
    prefix='/raw',
    tags=['raw']
)


@raw_router.post("/arrival")
async def arrival_raw(raw: Raw):
    return raw

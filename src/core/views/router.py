from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.schemas import CreateRaw
from src.core.schemas.raw_schemas import Raw
from src.core.services.raw_service import RawService
from src.database import db_helper


router = APIRouter(tags=["Raw"])


@router.post("/post_raw/", response_model=Raw,  status_code=status.HTTP_201_CREATED)
async def post_raw_into_base(
        raw_in: CreateRaw,
        raw_service: RawService = Depends(),
):
    return await raw_service.post_raw(raw_in=raw_in)

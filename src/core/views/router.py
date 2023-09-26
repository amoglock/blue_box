from fastapi import APIRouter, status, Depends

from src.core.schemas import CreateRaw
from src.core.schemas.raw_schemas import Raw
from src.core.services.raw_service import RawService


router = APIRouter(tags=["Raw"])


@router.post("/post_raw/", response_model=Raw,  status_code=status.HTTP_201_CREATED)
async def post_raw_into_base(
        raw_in: CreateRaw,
        raw_service: RawService = Depends(),
):

    """
    Post new entry to the database

    :param raw_in: incoming Raw instance as CreateRaw model
    :param raw_service: RawService instance
    :return: Raw model instance
    """

    return await raw_service.post_raw(raw_in=raw_in)


@router.get("/all_raw", response_model=list[Raw], status_code=status.HTTP_200_OK)
async def get_raw_list(
        raw_service: RawService = Depends(),
):

    """

    :param raw_service:
    :return:
    """

    return await raw_service.get_raw_list()

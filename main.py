from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database.database_helper import db_helper
from src.database.models import Base

from src.core.views.router import router as raw_router


@asynccontextmanager
async def lifespan(application: FastAPI):
    async with db_helper.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
        yield

app = FastAPI(lifespan=lifespan)

app.include_router(router=raw_router)

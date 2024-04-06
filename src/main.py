from fastapi import FastAPI
from src.raw_storage.routers.raw_router import raw_router
from src.database import create_db_and_tables

app = FastAPI()

create_db_and_tables()

app.include_router(raw_router)

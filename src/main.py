from fastapi import FastAPI
from src.raw_storage.routers.raw_router import raw_router

app = FastAPI()


app.include_router(raw_router)

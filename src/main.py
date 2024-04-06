from fastapi import FastAPI
from src.raw_storage.routers.raw_router import raw_router
import src.models
from src.database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

src.database.Base.metadata.create_all(bind=engine)

app.include_router(raw_router)

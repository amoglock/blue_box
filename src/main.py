from fastapi import FastAPI
from src.raw_storage.routers.raw_router import raw_router
import src.models
from src.database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

src.models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app.include_router(raw_router)

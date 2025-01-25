from fastapi import FastAPI

from frontend.routers.main_router import main_router
from src.orders_maker.routers.order_router import order_router
from src.product_maker.routers.product_router import product_router
from src.raw_storage.routers.raw_router import raw_router
from src.database import create_db_and_tables

app = FastAPI()

create_db_and_tables()

app.include_router(main_router)
app.include_router(raw_router)
app.include_router(order_router)
app.include_router(product_router)

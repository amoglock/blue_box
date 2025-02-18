from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from frontend.routers.main_router import main_router
from src.orders_maker.routers.order_router import order_router
from src.product_maker.routers.product_router import product_router
from src.semiproducts.routers.semiproduct_router import semiproduct_router
from src.raw_storage.routers.raw_router import raw_router
from src.database import create_db_and_tables

app = FastAPI()

static_path = Path(__file__).parent.parent / "frontend" / "static"

app.mount("/static", StaticFiles(directory=static_path), name="static")

create_db_and_tables()

app.include_router(main_router)
app.include_router(raw_router)
app.include_router(order_router)
app.include_router(product_router)
app.include_router(semiproduct_router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.v1 import products


app = FastAPI(title="Production Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# create_db_and_tables()

app.include_router(products.router)
# app.include_router(orders.router)
# app.include_router(raw_storage.router)
# app.include_router(semiproducts.router)

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}
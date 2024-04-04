import pytest
from httpx import AsyncClient, ASGITransport

from src.main import app
from src.raw_storage.models.models import IncomingRaw
from src.raw_storage.repository.repository import RawRepository

test_raw = {
    "title": "Dragon Fruit",
    "group": "string",
    "supplier": "Microsoft",
    "incoming_amount": 0,
    "delivery_date": "2024-02-19",
    "production_date": "2024-02-19",
    "expiration_date": "2024-02-19"
}


@pytest.mark.anyio
async def test_get_storage():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000/raw") as ac:
        response = await ac.get("/get_storage")
        assert response.status_code == 200
        assert response.json() == {
            "status": True,
            "message": "success",
            "data": {}
        }

        response = await ac.get("/get_storage?name=unknown_name")
        print(response.json())
        assert response.json() == {
            "status": False,
            "message": "Item unknown_name not found",
            "data": None
        }

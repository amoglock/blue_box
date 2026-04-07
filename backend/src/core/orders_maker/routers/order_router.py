from fastapi import APIRouter

order_router = APIRouter(
    prefix='/orders',
    tags=['orders'],
)


@order_router.get('')
async def get_orders():
    return {
        "order 12:00": {"pasta": 15, "potato": 45},
        "order 15:00": {"pasta": 20, "potato": 15},
    }

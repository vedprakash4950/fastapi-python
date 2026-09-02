from fastapi import APIRouter

from app.routers.vehicles import router as vehicle_router


api_router = APIRouter()

api_router.include_router(vehicle_router)
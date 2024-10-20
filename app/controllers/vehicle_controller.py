from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from services.auth_service import get_current_user
from config.db import db_dependency
from schemas.vehicle_schema import CreateVehicleRequest, VehicleResponse
from services.vehicle_service import VehicleService

token_auth_scheme = HTTPBearer()

vehicle_router = APIRouter(
    prefix="/vehicles",
    tags=["vehicles"],
)


@vehicle_router.get("")
def read_root():
    return {"message": "Hello World"}


@vehicle_router.post("", response_model=VehicleResponse)
def create_vehicle(
    vehicle: CreateVehicleRequest,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    vehicle_service = VehicleService(db)
    return vehicle_service.create_vehicle(vehicle, current_user["user_id"])

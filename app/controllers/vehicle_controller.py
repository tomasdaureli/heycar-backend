from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.db import get_db
from schemas.vehicle_schema import CreateVehicleRequest, VehicleResponse
from services.vehicle_service import VehicleService

vehicle_router = APIRouter()


@vehicle_router.get("/")
def read_root():
    return {"message": "Hello World"}


@vehicle_router.post("/vehicles", response_model=VehicleResponse)
def create_vehicle(vehicle: CreateVehicleRequest, db: Session = Depends(get_db)):
    vehicle_service = VehicleService(db)
    return vehicle_service.create_vehicle(vehicle)

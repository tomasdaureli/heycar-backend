from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.dto.schemas import CreateVehicleRequest, VehicleResponse
from app.service.service import VehicleService

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Hello World"}


@router.post("/vehicles", response_model=VehicleResponse)
def create_vehicle(vehicle: CreateVehicleRequest, db: Session = Depends(get_db)):
    vehicle_service = VehicleService(db)
    return vehicle_service.create_vehicle(vehicle)

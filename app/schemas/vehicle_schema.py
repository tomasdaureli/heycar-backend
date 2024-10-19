from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class VehicleType(Enum):
    CAR = "Car"
    TRUCK = "Truck"
    OTHER = "Other"


class CreateVehicleRequest(BaseModel):
    brand: str
    model: str
    vehicle_type: VehicleType
    license_plate: str
    year: int
    km: int


class VehicleResponse(BaseModel):
    id: int
    brand: str
    model: str
    vehicle_type: VehicleType
    license_plate: str
    year: int
    km: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

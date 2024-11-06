from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class VehicleType(Enum):
    CAR = "Car"
    TRUCK = "Truck"
    OTHER = "Other"


class State(str,Enum):
    OK = "OK"
    WARNING = "WARNING"
    CHECK = "CHECK"
    DANGER = "DANGER"


class CreateVehicleRequest(BaseModel):
    brand: str
    model: str
    vehicle_type: VehicleType
    license_plate: str
    year: int
    km: int


class UpdateVehicleStatusRequest(BaseModel):
    engine_status: State
    battery_status: State
    brakes_status: State
    tires_status: State
    oil_status: State
    temperature_status: State
    front_light_status: State
    rear_light_status: State


class VehicleResponse(BaseModel):
    id: int
    brand: str
    model: str
    vehicle_type: VehicleType
    license_plate: str
    year: int
    km: int
    engine_status: State | None
    battery_status: State | None
    brakes_status: State | None
    tires_status: State | None
    oil_status: State | None
    temperature_status: State | None
    front_light_status: State | None
    rear_light_status: State | None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

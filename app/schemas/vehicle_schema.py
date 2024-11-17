from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class VehicleType(Enum):
    CAR = "Car"
    TRUCK = "Truck"
    OTHER = "Other"


class State(str, Enum):
    OK = "OK"
    CHECK = "CHECK"
    DANGER = "DANGER"


class VehicleStatus(BaseModel):
    obd_code: str
    status: State


class CreateVehicleRequest(BaseModel):
    brand: str
    model: str
    vehicle_name: str
    vehicle_type: VehicleType
    license_plate: str
    year: int
    km: int


class UpdateVehicleStatusRequest(BaseModel):
    km: int
    engine_status: VehicleStatus
    battery_status: VehicleStatus
    brakes_status: VehicleStatus
    tires_status: VehicleStatus
    oil_status: VehicleStatus
    temperature_status: VehicleStatus
    front_light_status: VehicleStatus
    rear_light_status: VehicleStatus


class VehicleResponse(BaseModel):
    id: int
    brand: str
    model: str
    vehicle_name: str
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

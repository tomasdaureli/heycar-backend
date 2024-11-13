from typing import List
from fastapi import APIRouter, Depends
from app.schemas.failure_schema import FailureResponse, CreateFailureRequest
from app.services.failure_service import FailureService
from services.auth_service import get_current_user
from config.db import db_dependency
from schemas.vehicle_schema import (
    CreateVehicleRequest,
    UpdateVehicleStatusRequest,
    VehicleResponse,
)
from services.vehicle_service import VehicleService

vehicle_router = APIRouter(
    prefix="/vehicles",
    tags=["vehicles"],
)


@vehicle_router.post("", response_model=VehicleResponse, status_code=201)
def create_vehicle(
    vehicle: CreateVehicleRequest,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    vehicle_service = VehicleService(db)
    return vehicle_service.create_vehicle(vehicle, current_user["user_id"])


@vehicle_router.get("", response_model=List[VehicleResponse])
def get_vehicles(
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    vehicle_service = VehicleService(db)
    return vehicle_service.get_vehicles(current_user["user_id"])


@vehicle_router.post(
    "/{vehicle_id}/failures", status_code=201, response_model=FailureResponse
)
def create_failure(
    vehicle_id: int,
    failure: CreateFailureRequest,
    db: db_dependency,
):
    failure_service = FailureService(db)
    return failure_service.create_failure(vehicle_id, failure)


@vehicle_router.get("/{vehicle_id}/failures", response_model=List[FailureResponse])
def get_failures(vehicle_id: int, db: db_dependency):
    failure_service = FailureService(db)
    return failure_service.get_failures(vehicle_id)


@vehicle_router.get("/{vehicle_id}", response_model=VehicleResponse)
def get_actual_state(
    vehicle_id: int,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    vehicle_service = VehicleService(db)
    return vehicle_service.get_actual_state(vehicle_id)


@vehicle_router.put("/{vehicle_id}/actual-status", status_code=200)
def update_vehicle_status(
    vehicle_id: int,
    vehicle_status: UpdateVehicleStatusRequest,
    db: db_dependency,
):
    vehicle_service = VehicleService(db)
    return vehicle_service.update_vehicle_status(vehicle_id, vehicle_status)

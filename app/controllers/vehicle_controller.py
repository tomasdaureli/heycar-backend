from typing import List
from fastapi import APIRouter, Depends
from schemas.alert_schema import AlertResponse, CreateAlertRequest
from services.alert_service import AlertService
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
    "/{vehicle_id}/alerts", status_code=201, response_model=AlertResponse
)
def create_alert(
    vehicle_id: int,
    alert: CreateAlertRequest,
    db: db_dependency,
):
    alert_service = AlertService(db)
    return alert_service.create_alert(vehicle_id, alert)


@vehicle_router.get("/{vehicle_id}/alerts", response_model=List[AlertResponse])
def get_alerts(vehicle_id: int, db: db_dependency):
    alert_service = AlertService(db)
    return alert_service.get_alerts(vehicle_id)


@vehicle_router.get("/{vehicle_id}/actual-status", response_model=VehicleResponse)
def get_actual_state(
    vehicle_id: int,
    vehicle_status: UpdateVehicleStatusRequest,
    db: db_dependency,
):
    vehicle_service = VehicleService(db)
    return vehicle_service.get_actual_state(vehicle_id, vehicle_status)

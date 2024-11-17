from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from services.repair_service import RepairService
from schemas.repair_schema import CreateRepairRequest, RepairResponse
from config.db import db_dependency
from services.auth_service import get_current_user

repair_router = APIRouter(
    prefix="/repairs",
    tags=["repairs"],
)


@repair_router.post("", response_model=RepairResponse, status_code=201)
def create_repair(
    repair: CreateRepairRequest,
    db: Session = Depends(db_dependency),
    current_user=Depends(get_current_user),
):
    repair_service = RepairService(db)
    return repair_service.create_repair(repair, current_user.user_id)


@repair_router.get("/{vehicle_id}", response_model=List[RepairResponse])
def get_repairs(
    vehicle_id: int,
    db: Session = Depends(db_dependency),
    date_from: Optional[str] = Query(
        None, description="Filter by date from (YYYY-MM-DD)"
    ),
    date_to: Optional[str] = Query(
        None, description="Filter by date from (YYYY-MM-DD)"
    ),
    repair_type: Optional[str] = Query(
        None, description="Repair type (maintenance, repair, upgrade)"
    ),
):
    repair_service = RepairService(db)
    return repair_service.get_repairs(vehicle_id, date_from, date_to, repair_type)


@repair_router.get("/{repair_id}", response_model=RepairResponse)
def get_repair(repair_id: int, db: Session = Depends(db_dependency)):
    repair_service = RepairService(db)
    return repair_service.get_repair(repair_id)


@repair_router.put("/{repair_id}", response_model=RepairResponse)
def update_repair(
    repair_id: int, repair: CreateRepairRequest, db: Session = Depends(db_dependency)
):
    repair_service = RepairService(db)
    return repair_service.update_repair(repair_id, repair)


@repair_router.delete("/{repair_id}", response_model=RepairResponse)
def delete_repair(repair_id: int, db: Session = Depends(db_dependency)):
    repair_service = RepairService(db)
    return repair_service.delete_repair(repair_id)

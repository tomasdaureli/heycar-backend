from fastapi import APIRouter, Depends
from services.auth_service import get_current_user
from config.db import db_dependency
from services.alert_service import AlertService

alert_router = APIRouter(
    prefix="/alerts",
    tags=["alerts"],
)



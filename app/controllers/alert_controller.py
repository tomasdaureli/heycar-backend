from fastapi import APIRouter, Depends
from models.user_model import User
from schemas.alert_schema import AlertResponse, FixAlertRequest
from services.auth_service import get_current_user
from config.db import db_dependency
from services.alert_service import AlertService

alert_router = APIRouter(
    prefix="/alerts",
    tags=["alerts"],
)


@alert_router.post("/{alert_id}/fixes", status_code=200, response_model=AlertResponse)
def fix_alert(
    alert_id: int,
    request: FixAlertRequest,
    db: db_dependency,
    current_user: User = Depends(get_current_user),
):
    alert_service = AlertService(db)
    return alert_service.fix_alert(alert_id, request.fixed)

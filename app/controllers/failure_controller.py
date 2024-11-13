from fastapi import APIRouter, Depends
from models.user_model import User
from schemas.failure_schema import FailureResponse, FixFailureRequest
from services.auth_service import get_current_user
from config.db import db_dependency
from services.failure_service import FailureService

failure_router = APIRouter(
    prefix="/failures",
    tags=["failures"],
)


@failure_router.post(
    "/{failure_id}/fixes", status_code=200, response_model=FailureResponse
)
def fix_failure(
    failure_id: int,
    request: FixFailureRequest,
    db: db_dependency,
    current_user: User = Depends(get_current_user),
):
    failure_service = FailureService(db)
    return failure_service.fix_failure(failure_id, request.fixed)

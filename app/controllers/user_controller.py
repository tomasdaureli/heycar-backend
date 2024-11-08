from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.badges_schema import (
    BadgeCreateRequest,
    BadgeResponse,
    LevelsResponse,
    PointsResponse,
)
from services.auth_service import get_current_user
from schemas.user_schema import CreateUserRequest, UserResponse
from config.db import db_dependency
from services.user_service import UserService
from config.notifications import (
    PushNotificationPayload,
    send_push_notification_firebase,
    send_push_notification_expo,
)

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@user_router.post("", response_model=UserResponse, status_code=201)
def create_user(user: CreateUserRequest, db: db_dependency):
    user_service = UserService(db)
    return user_service.create_user(user)


@user_router.get("/me", response_model=UserResponse)
def get_user(db: db_dependency, current_user: dict = Depends(get_current_user)):
    user_service = UserService(db)
    return user_service.get_user(current_user["user_id"])


@user_router.get("/{user_id}/points", response_model=PointsResponse)
def get_user_points(user_id: int, db: db_dependency):
    user_service = UserService(db)
    points = user_service.get_user_points(user_id)
    return PointsResponse(points=points)


@user_router.get("/{user_id}/levels", response_model=LevelsResponse)
def get_user_levels(user_id: int, db: db_dependency):
    user_service = UserService(db)
    level = user_service.get_user_levels(user_id)
    return LevelsResponse(level=level)


@user_router.get("/{user_id}/badges", response_model=List[BadgeResponse])
def get_user_badges(user_id: int, db: db_dependency):
    badge_service = UserService(db)
    return badge_service.get_user_badges(user_id)


@user_router.post("/{user_id}/badges", response_model=BadgeResponse)
def assign_badge(user_id: int, badge_request: BadgeCreateRequest, db: db_dependency):
    badge_service = UserService(db)
    return badge_service.assign_badge(
        user_id,
        badge_request.badge_name,
        badge_request.description,
        badge_request.score,
    )


@user_router.post("/send-notification")
async def send_notification(payload: PushNotificationPayload):
    # result = send_push_notification_firebase(payload.token, payload.title, payload.body)
    result = send_push_notification_expo(payload.token, payload.title, payload.body)
    return {"status": "success", "result": result}

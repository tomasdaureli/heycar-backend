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
import json
from config.notifications import (
    PushNotificationPayload,
    send_notification,
)
import requests

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
    # result = send_push_notification(
    #     "d22stUVBTqi1PSlngeu6ah:APA91bENLim9rrZhpSZsybug3YNjfK0cEjNgeEyn9nM6NVx17q7cd-aRqPv2Gz5zt9y0wHahgBOhTeuq35Pl7EP2iFcDI9908_nSKyxDVFsPZQpYrjSVsuhlquJt-_nES1jAmudgPvAX",
    #     "Prueba",
    #     "Este es un mensaje de prueba",
    # )
    # return {"status": "success", "result": result}

    return send_notification(payload)

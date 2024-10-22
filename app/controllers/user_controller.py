from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.auth_service import get_current_user
from schemas.user_schema import AchievementResponse, CreateUserRequest, UserResponse
from config.db import db_dependency
from services.user_service import UserService

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


@user_router.get("/achievements", response_model=List[AchievementResponse])
def get_user_achievements(
    db: db_dependency, current_user: dict = Depends(get_current_user)
):
    user_service = UserService(db)
    return user_service.get_user_achievements(current_user["user_id"])

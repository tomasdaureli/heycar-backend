from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.auth_service import get_current_user
from schemas.user_schema import CreateUserRequest, UserResponse
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

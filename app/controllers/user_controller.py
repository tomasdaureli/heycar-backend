from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user_schema import CreateUserRequest, UserResponse
from config.db import db_dependency
from services.user_service import UserService

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@user_router.post("", response_model=UserResponse)
def create_user(user: CreateUserRequest, db: db_dependency):
    user_service = UserService(db)
    return user_service.create_user(user)

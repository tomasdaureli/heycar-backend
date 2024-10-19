from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user_schema import CreateUserRequest, UserResponse
from config.db import get_db
from services.user_service import UserService

user_router = APIRouter()


@user_router.post("/users", response_model=UserResponse)
def create_user(user: CreateUserRequest, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.create_user(user)

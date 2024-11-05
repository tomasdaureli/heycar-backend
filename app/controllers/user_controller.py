from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.auth_service import get_current_user
from schemas.user_schema import CreateUserRequest, UserResponse
from config.db import db_dependency
from services.user_service import UserService
from config.notifications import send_push_notification

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


@user_router.post("/send-notification")
async def send_notification():
    result = send_push_notification(
        "thw-s6A2jx79Oa1u7ScNJ5B2rm0jMxz04Ih_qsiOato",
        "Prueba",
        "Este es un mensaje de prueba",
    )
    return {"status": "success", "result": result}

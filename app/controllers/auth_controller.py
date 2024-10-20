from fastapi import APIRouter
from schemas.auth_schema import Token
from schemas.user_schema import LoginUserRequest
from services.auth_service import create_access_token, authenticate_user
from config.db import db_dependency


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@auth_router.post("/token", response_model=Token)
def login_for_access_token(request: LoginUserRequest, db: db_dependency):
    user = authenticate_user(request.email, request.password, db)
    token = create_access_token(user.id, user.email)
    return {"access_token": token, "token_type": "bearer"}

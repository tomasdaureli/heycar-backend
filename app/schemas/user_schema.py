from pydantic import BaseModel, EmailStr
from datetime import datetime


class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class LoginUserRequest(BaseModel):
    email: str
    password: str


class UserNotificationToken(BaseModel):
    token: str
    type: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    level: int | None
    points: int | None
    created_at: datetime
    updated_at: datetime
    notification_token: str | None
    notification_type: str | None

    class Config:
        orm_mode = True

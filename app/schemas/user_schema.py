from pydantic import BaseModel, EmailStr
from datetime import datetime


class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class LoginUserRequest(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    level: int | None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class AchievementResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True

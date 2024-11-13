from pydantic import BaseModel
from datetime import datetime


class CreateFailureRequest(BaseModel):
    title: str
    part: str
    description: str
    severity: str


class FixFailureRequest(BaseModel):
    fixed: bool


class FailureResponse(BaseModel):
    id: int
    title: str
    part: str
    description: str
    severity: str
    fixed: bool
    created_at: datetime

    class Config:
        from_attributes = True

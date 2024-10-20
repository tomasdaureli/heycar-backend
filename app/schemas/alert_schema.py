from pydantic import BaseModel
from datetime import datetime


class CreateAlertRequest(BaseModel):
    title: str
    part: str
    description: str
    severity: str


class AlertResponse(BaseModel):
    id: int
    title: str
    part: str
    description: str
    severity: str
    fixed: bool
    created_at: datetime

    class Config:
        from_attributes = True

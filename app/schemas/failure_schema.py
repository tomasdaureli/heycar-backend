from enum import Enum
from pydantic import BaseModel
from datetime import datetime


class ReportType(str, Enum):
    MANUAL = "manual"
    AUTOMATIC = "automatic"


class CreateFailureRequest(BaseModel):
    title: str
    part: str
    description: str
    severity: str
    date: datetime
    km: int
    report_type: ReportType
    fixed: bool


class FixFailureRequest(BaseModel):
    fixed: bool


class FailureResponse(BaseModel):
    id: int
    title: str
    part: str
    description: str
    severity: str
    km: int
    report_type: ReportType | None
    fixed: bool
    solution: str
    created_at: datetime

    class Config:
        from_attributes = True
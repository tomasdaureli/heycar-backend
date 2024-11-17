from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime


class ReportType(str, Enum):
    MANUAL = "manual"
    AUTOMATIC = "automatic"


class CreateFailureRequest(BaseModel):
    title: str
    part: str
    description: str
    km: int
    report_type: ReportType = Field(default=ReportType.MANUAL)


class FixFailureRequest(BaseModel):
    fixed: bool


class FailureResponse(BaseModel):
    id: int
    title: str
    part: str
    description: str
    km: int
    report_type: ReportType | None
    fixed: bool
    solution: str | None
    created_at: datetime

    class Config:
        from_attributes = True

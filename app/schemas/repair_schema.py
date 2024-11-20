from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime


class RepairType(str, Enum):
    MAINTENANCE = "maintenance"
    REPAIR = "repair"
    UPGRADE = "upgrade"


class CreateRepairRequest(BaseModel):
    date: datetime
    part: str
    description: str
    cost: float
    repair_vehicle_id: int
    type: RepairType = Field(default=RepairType.REPAIR)


class UpdateRepairRequest(BaseModel):
    description: str
    cost: float
    type: RepairType = Field(default=RepairType.REPAIR)


class RepairResponse(BaseModel):
    id: int
    date: datetime
    part: str
    description: str
    cost: float
    repair_vehicle_id: int
    repair_user_id: int
    type: RepairType
    created_at: datetime

    class Config:
        orm_mode = True

from pydantic import BaseModel
from datetime import datetime


class CreateVehicleRequest(BaseModel):
    name: str
    email: str


class VehicleResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

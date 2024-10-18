from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from app.config.db import SessionLocal
from app.dto.schemas import CreateVehicleRequest, VehicleResponse
from app.service.service import VehicleService
from app.router.controller import router

app = FastAPI()

app.include_router(router)

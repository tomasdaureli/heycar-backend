from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.schemas import CreateVehicleRequest, VehicleResponse
from app.service import VehicleService
from app.controller import router

app = FastAPI()

app.include_router(router)

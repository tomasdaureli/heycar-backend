from sqlalchemy.orm import Session
from app.models import Vehicle
from app.schemas import CreateVehicleRequest


class VehicleService:
    def __init__(self, db: Session):
        self.db = db

    def create_vehicle(self, vehicle: CreateVehicleRequest):
        db_vehicle = Vehicle(name=vehicle.name, email=vehicle.email)
        self.db.add(db_vehicle)
        self.db.commit()
        self.db.refresh(db_vehicle)
        return db_vehicle

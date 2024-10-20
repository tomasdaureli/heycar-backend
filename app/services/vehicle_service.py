from sqlalchemy.orm import Session
from models.vehicle_model import Vehicle
from schemas.vehicle_schema import CreateVehicleRequest


class VehicleService:
    def __init__(self, db: Session):
        self.db = db

    def create_vehicle(self, vehicle: CreateVehicleRequest, user_id: int):
        db_vehicle = Vehicle(
            brand=vehicle.brand,
            model=vehicle.model,
            vehicle_type=vehicle.vehicle_type.value,
            license_plate=vehicle.license_plate,
            year=vehicle.year,
            km=vehicle.km,
            user_id=user_id,
        )
        self.db.add(db_vehicle)
        self.db.commit()
        self.db.refresh(db_vehicle)
        return db_vehicle

    def get_vehicles(self, user_id: int):
        return self.db.query(Vehicle).filter(Vehicle.user_id == user_id).all()

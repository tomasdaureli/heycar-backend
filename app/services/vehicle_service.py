from sqlalchemy.orm import Session
from models.vehicle_model import Vehicle
from schemas.vehicle_schema import CreateVehicleRequest, UpdateVehicleStatusRequest


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

    def get_actual_state(self, vehicle_id: int):
        vehicle = self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
        if not vehicle:
            raise ValueError("Vehicle not found")
        return vehicle

    def update_vehicle_status(
        self, vehicle_id: int, vehicle_status: UpdateVehicleStatusRequest
    ):
        vehicle = self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
        if not vehicle:
            raise ValueError("Vehicle not found")

        vehicle.engine_status = vehicle_status.engine_status
        vehicle.battery_status = vehicle_status.battery_status
        vehicle.brakes_status = vehicle_status.brakes_status
        vehicle.tires_status = vehicle_status.tires_status
        vehicle.oil_status = vehicle_status.oil_status
        vehicle.temperature_status = vehicle_status.temperature_status
        vehicle.front_light_status = vehicle_status.front_light_status
        vehicle.rear_light_status = vehicle_status.rear_light_status

        self.db.commit()
        self.db.refresh(vehicle)

        return vehicle

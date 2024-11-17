from sqlalchemy.orm import Session
from models.user_model import User
from schemas.failure_schema import CreateFailureRequest, ReportType
from models.vehicle_model import Vehicle
from models.notification_model import Notification
from schemas.vehicle_schema import (
    CreateVehicleRequest,
    State,
    UpdateVehicleStatusRequest,
)
from config.notifications import (
    send_push_notification_expo,
    send_push_notification_firebase,
)
from services import failure_service
import json


with open("obd-trouble-codes.json", "r") as file:
    obd_codes_list = json.load(file)

obd_codes = {item["obd_code"]: item["message"] for item in obd_codes_list}


class VehicleService:
    def __init__(self, db: Session):
        self.db = db

    def create_vehicle(self, vehicle: CreateVehicleRequest, user_id: int):
        db_vehicle = Vehicle(
            brand=vehicle.brand,
            model=vehicle.model,
            vehicle_name=vehicle.vehicle_name,
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

        user = self.db.query(User).filter(User.id == vehicle.user_id).first()
        for field_name, value in vehicle_status.dict().items():
            if isinstance(value, dict) and value.get("status") == State.DANGER:
                message = self._get_odb_code_message(value.get("obd_code"))
                failure = self._add_failure(
                    vehicle_id, vehicle_status, vehicle, field_name, message
                )
                self.notify_user(vehicle, user, field_name, message, failure)

        vehicle.km = vehicle_status.km
        vehicle.engine_status = vehicle_status.engine_status.status
        vehicle.battery_status = vehicle_status.battery_status.status
        vehicle.brakes_status = vehicle_status.brakes_status.status
        vehicle.tires_status = vehicle_status.tires_status.status
        vehicle.oil_status = vehicle_status.oil_status.status
        vehicle.temperature_status = vehicle_status.temperature_status.status
        vehicle.front_light_status = vehicle_status.front_light_status.status
        vehicle.rear_light_status = vehicle_status.rear_light_status.status

        self.db.commit()
        self.db.refresh(vehicle)

        return vehicle

    def _get_odb_code_message(self, obd_code: str):
        return obd_codes.get(obd_code, "Unknown issue")

    def _add_failure(self, vehicle_id, vehicle_status, vehicle, field_name, message):
        failure_request = CreateFailureRequest(
            title=f"{vehicle.vehicle_name}. {field_name} is in danger",
            part=field_name,
            description=message,
            km=vehicle_status.km,
            report_type=ReportType.AUTOMATIC,
        )
        return failure_service.FailureService(self.db).create_failure(
            vehicle_id=vehicle_id, failure=failure_request
        )

    def notify_user(self, vehicle, user, field_name, message, failure):
        if user.notification_type == "expo":
            send_push_notification_expo(
                user.notification_token,
                f"{vehicle.vehicle_name}: Isuue encountered in {field_name}",
                message,
            )
        else:
            send_push_notification_firebase(
                user.notification_token,
                f"{vehicle.vehicle_name}: Isuue encountered in {field_name}",
                message,
            )
        notification = Notification(
            failure_id=failure.id if failure else None, user_id=user.id
        )
        self.db.add(notification)
        self.db.commit()
        self.db.refresh(notification)

from sqlalchemy.orm import Session

from schemas.alert_schema import CreateAlertRequest
from models.alert_model import Alert


class AlertService:
    def __init__(self, db: Session):
        self.db = db

    def create_alert(self, vehicle_id: int, alert: CreateAlertRequest):
        new_alert = Alert(
            vehicle_id=vehicle_id,
            title=alert.title,
            part=alert.part,
            description=alert.description,
            severity=alert.severity,
        )
        self.db.add(new_alert)
        self.db.commit()
        return new_alert

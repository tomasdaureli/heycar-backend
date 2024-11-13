from sqlalchemy.orm import Session

from schemas.failure_schema import CreateFailureRequest
from models.failure_model import Failure


class FailureService:
    def __init__(self, db: Session):
        self.db = db

    def create_failure(self, vehicle_id: int, failure: CreateFailureRequest):
        new_failure = Failure(
            vehicle_id=vehicle_id,
            title=failure.title,
            part=failure.part,
            description=failure.description,
            severity=failure.severity,
        )
        self.db.add(new_failure)
        self.db.commit()
        return new_failure

    def fix_failure(self, failure_id: int, fixed: bool):
        failure = self.db.query(Failure).filter(Failure.id == failure_id).first()
        failure.fixed = fixed
        self.db.commit()
        return failure

    def get_failures(self, vehicle_id: int):
        return self.db.query(Failure).filter(Failure.vehicle_id == vehicle_id).all()

from sqlalchemy.orm import Session

from schemas.repair_schema import (
    CreateRepairRequest,
    RepairResponse,
    UpdateRepairRequest,
)
from models.repair_model import Repair


class RepairService:
    def __init__(self, db: Session):
        self.db = db

    def create_repair(self, repair: CreateRepairRequest, user_id: int):
        db_repair = Repair(
            date=repair.date,
            part=repair.part,
            description=repair.description,
            cost=repair.cost,
            repair_vehicle_id=repair.repair_vehicle_id,
            repair_user_id=user_id,
            type=repair.type.value,
        )
        self.db.add(db_repair)
        self.db.commit()
        self.db.refresh(db_repair)
        return db_repair

    def get_repairs(
        self, vehicle_id: int, date_from: str, date_to: str, repair_type: str
    ):
        query = self.db.query(Repair).filter(Repair.repair_vehicle_id == vehicle_id)
        if date_from:
            query = query.filter(Repair.date >= date_from)
        if date_to:
            query = query.filter(Repair.date <= date_to)
        if repair_type:
            query = query.filter(Repair.type == repair_type)
        return query.all()

    def get_repair(self, repair_id: int):
        return self.db.query(Repair).filter(Repair.id == repair_id).first()

    def update_repair(self, repair_id: int, repair: UpdateRepairRequest):
        db_repair = self.db.query(Repair).filter(Repair.id == repair_id).first()
        db_repair.description = repair.description
        db_repair.cost = repair.cost
        db_repair.type = repair.type
        self.db.commit()
        return db_repair

    def delete_repair(self, repair_id: int):
        db_repair = self.db.query(Repair).filter(Repair.id == repair_id).first()
        self.db.delete(db_repair)
        self.db.commit()
        return db_repair

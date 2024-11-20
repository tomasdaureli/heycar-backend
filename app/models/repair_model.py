from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Date,
    DateTime,
    ForeignKey,
    Numeric,
)
from sqlalchemy.orm import relationship
from config.db import Base
from datetime import datetime


class Repair(Base):
    __tablename__ = "repairs"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    part = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    cost = Column(Numeric(10, 2), nullable=False)
    repair_vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    repair_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    vehicle = relationship("Vehicle", back_populates="repairs")
    user = relationship("User", back_populates="repairs")

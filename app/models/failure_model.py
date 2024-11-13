from sqlalchemy import Column, Integer, String, DateTime, Boolean
from config.db import Base
from datetime import datetime


class Failure(Base):
    __tablename__ = "failures"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    part = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    severity = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    fixed = Column(Boolean, default=False)

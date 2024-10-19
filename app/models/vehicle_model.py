from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from config.db import Base
from datetime import datetime


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(255), nullable=False)
    model = Column(String(255), nullable=False)
    vehicle_type = Column(String(255), nullable=False)
    license_plate = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    km = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

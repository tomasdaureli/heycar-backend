from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Boolean
from config.db import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    level = Column(Integer, default=1, nullable=True)
    points = Column(Integer, default=0, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    badges = relationship("Badge", back_populates="user")
    notification_token = Column(String(255), nullable=True)
    notification_type = Column(String(255), nullable=True)
    notifications = relationship(
        "Notification", back_populates="user", cascade="all, delete-orphan"
    )
    repairs = relationship("Repair", back_populates="user", cascade="all, delete-orphan")

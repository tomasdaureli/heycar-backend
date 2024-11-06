from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Boolean
from config.db import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Badge(Base):
    __tablename__ = 'badges'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True) 
    description = Column(String) 
    score = Column(Integer, default=0)  
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="badges")

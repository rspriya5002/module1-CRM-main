# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
import datetime
from .database import Base

class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True, index=True)
    status = Column(String, default="new")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Deal(Base):
    __tablename__ = "deals"
    id = Column(Integer, primary_key=True)
    lead_id = Column(Integer, ForeignKey("leads.id"), nullable=False, index=True)
    value_cents = Column(Integer, nullable=False)
    seller_id = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())  
    lead = relationship("Lead")

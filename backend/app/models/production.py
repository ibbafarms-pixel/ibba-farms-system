"""Production record model."""

from sqlalchemy import Column, String, Integer, Float, DateTime, Date, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime, date
import uuid
from app.database import Base


class ProductionRecord(Base):
    """Daily egg production record."""
    __tablename__ = "production_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date = Column(Date, nullable=False, index=True)
    house_id = Column(UUID(as_uuid=True), ForeignKey("houses.id"), nullable=False, index=True)
    number_of_birds = Column(Integer, nullable=False)
    eggs_collected = Column(Integer, nullable=False)
    broken_eggs = Column(Integer, default=0)
    cracked_eggs = Column(Integer, default=0)
    good_eggs = Column(Integer, nullable=False)
    mortality = Column(Integer, default=0)
    birds_culled = Column(Integer, default=0)
    water_consumption_liters = Column(Integer, default=0)
    feed_used_kg = Column(Float, nullable=False)
    production_percentage = Column(Float, nullable=False)
    notes = Column(Text)
    recorded_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

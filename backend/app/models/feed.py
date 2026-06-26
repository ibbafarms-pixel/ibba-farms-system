"""Feed inventory models."""

from sqlalchemy import Column, Float, DateTime, Date, ForeignKey, Text, Enum, String
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, date
import uuid
from app.database import Base
from enum import Enum as PyEnum


class FeedTransactionType(str, PyEnum):
    """Feed transaction types."""
    PURCHASE = "purchase"
    CONSUMPTION = "consumption"


class FeedInventory(Base):
    """Current feed inventory level."""
    __tablename__ = "feed_inventory"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    current_stock_kg = Column(Float, default=0, nullable=False)
    minimum_threshold_kg = Column(Float, default=2000, nullable=False)
    average_cost_per_kg = Column(Float)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class FeedTransaction(Base):
    """Feed inventory transaction."""
    __tablename__ = "feed_transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = Column(Enum(FeedTransactionType), nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    quantity_kg = Column(Float, nullable=False)
    price_per_kg = Column(Float)
    total_cost = Column(Float)
    stock_before_kg = Column(Float, nullable=False)
    stock_after_kg = Column(Float, nullable=False)
    reference_type = Column(String(50))
    reference_id = Column(UUID(as_uuid=True))
    supplier_id = Column(UUID(as_uuid=True), ForeignKey("suppliers.id"))
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

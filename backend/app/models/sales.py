"""Sales models."""

from sqlalchemy import Column, String, Integer, Float, DateTime, Date, ForeignKey, Boolean, Text, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime, date
import uuid
from app.database import Base
from enum import Enum as PyEnum


class PaymentMethod(str, PyEnum):
    """Payment methods."""
    CASH = "cash"
    CHECK = "check"
    MOBILE_MONEY = "mobile_money"
    BANK_TRANSFER = "bank_transfer"
    CREDIT = "credit"


class Customer(Base):
    """Customer model."""
    __tablename__ = "customers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False, index=True)
    phone = Column(String(20), index=True)
    email = Column(String(255))
    location = Column(String(255))
    contact_person = Column(String(255))
    credit_limit = Column(Float, default=0)
    current_balance = Column(Float, default=0)
    is_active = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SalesRecord(Base):
    """Egg sales record."""
    __tablename__ = "sales_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"), nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    trays = Column(Integer, default=0)
    loose_eggs = Column(Integer, default=0)
    total_eggs = Column(Integer, nullable=False)
    price_per_unit = Column(Integer, nullable=False)
    total_revenue = Column(Integer, nullable=False)
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    paid = Column(Boolean, default=False, index=True)
    invoice_number = Column(String(100), unique=True)
    notes = Column(Text)
    recorded_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

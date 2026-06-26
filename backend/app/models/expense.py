"""Expense models."""

from sqlalchemy import Column, String, Float, DateTime, Date, ForeignKey, Boolean, Text, Enum
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, date
import uuid
from app.database import Base
from enum import Enum as PyEnum


class ExpenseCategory(str, PyEnum):
    """Expense categories."""
    FEED = "feed"
    VACCINES = "vaccines"
    FUEL = "fuel"
    ELECTRICITY = "electricity"
    LABOUR = "labour"
    REPAIRS = "repairs"
    TRANSPORT = "transport"
    PACKAGING = "packaging"
    MEDICINE = "medicine"
    WATER = "water"
    INTERNET = "internet"
    PHONE = "phone"
    OTHER = "other"


class PaymentMethod(str, PyEnum):
    """Payment methods."""
    CASH = "cash"
    CHECK = "check"
    MOBILE_MONEY = "mobile_money"
    BANK_TRANSFER = "bank_transfer"


class Supplier(Base):
    """Supplier model."""
    __tablename__ = "suppliers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(20))
    email = Column(String(255))
    contact_person = Column(String(255))
    specialization = Column(String(100))
    is_active = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ExpenseRecord(Base):
    """Expense record."""
    __tablename__ = "expense_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category = Column(Enum(ExpenseCategory), nullable=False, index=True)
    supplier_id = Column(UUID(as_uuid=True), ForeignKey("suppliers.id"))
    date = Column(Date, nullable=False, index=True)
    amount = Column(Float, nullable=False)
    currency = Column(String(3), default="RWF")
    description = Column(Text)
    invoice_number = Column(String(100))
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    paid = Column(Boolean, default=False, index=True)
    notes = Column(Text)
    recorded_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

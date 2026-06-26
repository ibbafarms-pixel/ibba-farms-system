"""Data validation utilities."""

from datetime import date
from typing import Optional
from app.utils.exceptions import ValidationException


def validate_date_range(start_date: date, end_date: date) -> None:
    """Validate date range.
    
    Args:
        start_date: Start date
        end_date: End date
    
    Raises:
        ValidationException: If date range is invalid
    """
    if start_date > end_date:
        raise ValidationException(
            "Start date must be before end date",
            {"start_date": "Must be before end_date"}
        )


def validate_future_date(target_date: date) -> None:
    """Validate that date is not in the future.
    
    Args:
        target_date: Date to validate
    
    Raises:
        ValidationException: If date is in future
    """
    if target_date > date.today():
        raise ValidationException(
            "Date cannot be in the future",
            {"date": "Cannot be in the future"}
        )


def validate_positive_integer(value: int, field_name: str) -> None:
    """Validate positive integer.
    
    Args:
        value: Value to validate
        field_name: Name of field for error message
    
    Raises:
        ValidationException: If value is not positive
    """
    if value < 0:
        raise ValidationException(
            f"{field_name} must be non-negative",
            {field_name.lower(): "Must be non-negative"}
        )


def validate_positive_decimal(value: float, field_name: str) -> None:
    """Validate positive decimal.
    
    Args:
        value: Value to validate
        field_name: Name of field for error message
    
    Raises:
        ValidationException: If value is not positive
    """
    if value <= 0:
        raise ValidationException(
            f"{field_name} must be positive",
            {field_name.lower(): "Must be positive"}
        )

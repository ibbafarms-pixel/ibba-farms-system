"""Business calculation utilities."""

from decimal import Decimal
from typing import Optional


def calculate_production_percentage(
    eggs_collected: int,
    number_of_birds: int,
) -> float:
    """Calculate production percentage (eggs per bird).
    
    Args:
        eggs_collected: Number of eggs collected
        number_of_birds: Number of live birds
    
    Returns:
        Production percentage
    """
    if number_of_birds == 0:
        return 0.0
    return round((eggs_collected / number_of_birds) * 100, 2)


def calculate_good_eggs(
    eggs_collected: int,
    broken_eggs: int,
    cracked_eggs: int,
) -> int:
    """Calculate number of good eggs.
    
    Args:
        eggs_collected: Total eggs collected
        broken_eggs: Number of broken eggs
        cracked_eggs: Number of cracked eggs
    
    Returns:
        Number of good eggs
    """
    return eggs_collected - broken_eggs - cracked_eggs


def calculate_total_eggs(trays: int, loose_eggs: int) -> int:
    """Calculate total eggs from trays and loose eggs.
    
    Args:
        trays: Number of 30-egg trays
        loose_eggs: Number of loose eggs
    
    Returns:
        Total number of eggs
    """
    return (trays * 30) + loose_eggs


def calculate_total_revenue(
    total_eggs: int,
    price_per_unit: int,
) -> int:
    """Calculate total revenue from egg sales.
    
    Args:
        total_eggs: Total number of eggs
        price_per_unit: Price per egg (in RWF)
    
    Returns:
        Total revenue
    """
    return total_eggs * price_per_unit


def calculate_feed_cost(
    feed_used_kg: Decimal,
    price_per_kg: Decimal,
) -> Decimal:
    """Calculate total feed cost.
    
    Args:
        feed_used_kg: Kilograms of feed used
        price_per_kg: Price per kilogram
    
    Returns:
        Total feed cost
    """
    return (feed_used_kg * price_per_kg).quantize(Decimal('0.01'))


def calculate_daily_profit(
    revenue: int,
    feed_cost: int,
    other_expenses: int,
) -> int:
    """Calculate daily profit.
    
    Args:
        revenue: Daily revenue
        feed_cost: Daily feed cost
        other_expenses: Other daily expenses
    
    Returns:
        Daily profit
    """
    return revenue - feed_cost - other_expenses

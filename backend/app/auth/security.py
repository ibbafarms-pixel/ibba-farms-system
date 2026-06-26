"""Password hashing and verification."""

import bcrypt
from typing import Tuple


def hash_password(password: str) -> str:
    """Hash password using bcrypt.
    
    Args:
        password: Plain text password
    
    Returns:
        Hashed password
    """
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """Verify password against hash.
    
    Args:
        password: Plain text password to verify
        hashed_password: Hashed password to compare against
    
    Returns:
        True if password matches, False otherwise
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

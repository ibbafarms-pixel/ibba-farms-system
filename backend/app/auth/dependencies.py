"""Authentication dependencies for FastAPI."""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.jwt_handler import decode_token
from app.utils.exceptions import UnauthorizedException

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    """Get current authenticated user from JWT token.
    
    Args:
        credentials: HTTP Bearer credentials
        db: Database session
    
    Returns:
        Current user object
    
    Raises:
        UnauthorizedException: If token is invalid
    """
    try:
        payload = decode_token(credentials.credentials)
        user_id = payload.get("sub")
        
        if user_id is None:
            raise UnauthorizedException("Invalid token")
        
        # TODO: Query user from database
        # For now, return payload
        return payload
    except UnauthorizedException:
        raise
    except Exception:
        raise UnauthorizedException("Invalid credentials")


def require_role(*allowed_roles: str):
    """Dependency to check if user has required role.
    
    Args:
        allowed_roles: Tuple of allowed roles
    
    Returns:
        Dependency function
    """
    async def check_role(user = Depends(get_current_user)):
        user_role = user.get("role")
        if user_role not in allowed_roles:
            raise UnauthorizedException("Insufficient permissions")
        return user
    
    return check_role

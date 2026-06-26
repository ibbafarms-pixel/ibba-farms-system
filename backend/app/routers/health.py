"""Health check endpoint."""

from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check():
    """Health check endpoint.
    
    Returns:
        Health status
    """
    return {
        "status": "healthy",
        "version": "1.0.0",
    }


@router.get("/")
async def root():
    """Root endpoint.
    
    Returns:
        Welcome message
    """
    return {
        "message": "IBBA Farms Management System API",
        "version": "1.0.0",
        "docs": "/docs",
    }

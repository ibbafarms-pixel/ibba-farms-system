"""Global error handling middleware."""

from fastapi import Request, status
from fastapi.responses import JSONResponse
from app.utils.exceptions import AppException
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    """Handle application exceptions.
    
    Args:
        request: HTTP request
        exc: Application exception
    
    Returns:
        JSON response with error details
    """
    logger.error(
        f"AppException: {exc.code} - {exc.message}",
        extra={
            "code": exc.code,
            "status_code": exc.status_code,
            "path": request.url.path,
        }
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
                "details": exc.details,
                "timestamp": datetime.utcnow().isoformat(),
                "request_id": request.headers.get("X-Request-ID"),
            }
        },
    )


async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handle generic exceptions.
    
    Args:
        request: HTTP request
        exc: Generic exception
    
    Returns:
        JSON response with error details
    """
    logger.error(
        f"Unhandled exception: {str(exc)}",
        exc_info=True,
        extra={"path": request.url.path},
    )

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "Internal server error",
                "timestamp": datetime.utcnow().isoformat(),
                "request_id": request.headers.get("X-Request-ID"),
            }
        },
    )

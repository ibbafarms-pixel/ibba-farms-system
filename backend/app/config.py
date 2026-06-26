"""Application configuration management."""

from pydantic_settings import BaseSettings
from typing import List, Optional
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings from environment variables."""

    # Database
    database_url: str

    # Security
    secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_expire_hours: int = 24
    jwt_refresh_expire_days: int = 30

    # Application
    debug: bool = False
    app_name: str = "IBBA Farms Management System"
    app_version: str = "1.0.0"

    # CORS
    allowed_origins: str = "http://localhost:3000,http://localhost:5173"

    # Logging
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        case_sensitive = False

    @property
    def origins_list(self) -> List[str]:
        """Get allowed origins as list."""
        return [origin.strip() for origin in self.allowed_origins.split(",")]


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()

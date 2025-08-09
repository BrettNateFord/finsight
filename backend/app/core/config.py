# backend/app/core.py

from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl


class Settings(BaseSettings):
    PROJECT_NAME: str = "FinSight"
    PROJECT_VERSION: str = "1.0.0"
    FRONTEND_ORIGIN: AnyHttpUrl = "http://localhost:3000"  # React dev server
    
    API_KEY: str
    DATABASE_URL: str = "sqlite+aiosqlite:///./dev.db"  # Async SQLite for dev

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

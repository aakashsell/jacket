from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI React App"
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",  # React app
        "http://localhost:8000",  # FastAPI docs
    ]
    
    class Config:
        env_file = ".env"

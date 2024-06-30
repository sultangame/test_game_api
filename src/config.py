from pydantic_settings import BaseSettings, SettingsConfigDict
from motor.motor_asyncio import AsyncIOMotorClient
from src.models import QuestionODM
from beanie import init_beanie
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    DB_URL: str = "sqlite+aiosqlite:///db.sqlite3"
    PORT: int = 8000
    HOST: str = "localhost"
    DEBUG: bool = None
    RELOAD: bool = True

    async def initial_database(self):
        client = AsyncIOMotorClient(self.DB_URL)
        await init_beanie(client["test"], document_models=[QuestionODM])

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/app.env")


settings = Settings()

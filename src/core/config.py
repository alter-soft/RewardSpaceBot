from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://rewardspace:rewardspace@localhost:5432/rewardspace"
    website_url: str = "https://5tn9b2ff-3000.euw.devtunnels.ms/"
    bot_api: str

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parents[2] / ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()

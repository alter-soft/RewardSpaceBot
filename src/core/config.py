from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://rewardspace:rewardspace@localhost:5432/rewardspace"
    bot_api: str = "7800952850:AAEu9PsrUZIRfotwDmcmszqbmt38MkGMUjs"
    website_url: str = "https://5tn9b2ff-3000.euw.devtunnels.ms/"
    admins: list[int] = [802563179]


settings = Settings()

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "x402 Scheduler"

    APP_VERSION: str = "2.0.0"

    SERVICE_DESCRIPTION: str = "x402 Background Scheduler Service"

    ENVIRONMENT: str = "development"

    HOST: str = "0.0.0.0"

    PORT: int = 8000

    DEBUG: bool = False

    LOG_LEVEL: str = "INFO"

    API_PREFIX: str = "/api/v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()

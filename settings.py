from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from urllib.parse import quote_plus
from functools import lru_cache


class TgBotSettings(BaseSettings):
    token_secret_str: SecretStr = Field(..., alias="token")
    admin_ids: List[int]

    @property
    def token(self) -> str:
        """Get bot token as plain string."""
        return self.token_secret_str.get_secret_value()


class DatabaseSettings(BaseSettings):
    username: str
    password: SecretStr
    host: str
    port: int
    database: str

    @property
    def url(self) -> str:
        """Return properly formatted asyncpg connection URL."""
        password = quote_plus(self.password.get_secret_value())
        # postgresql[+asyncpg]://[user[:password]@][host][:port][/dbname][?param1=value1&param2=value2]
        return (
            f"postgresql+asyncpg://{self.username}:{password}"
            f"@{self.host}:{self.port}/{self.database}"
        )


class Settings(BaseSettings):
    tgbot: TgBotSettings
    db: DatabaseSettings

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore"
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Get cached application settings."""
    return Settings()

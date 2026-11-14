
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Roblox Shorts AI Studio"
    app_env: str = "development"
    debug: bool = True
    api_v1_prefix: str = "/api/v1"

    gemini_api_key: str = ""

    cors_origins: str = "http://localhost:3000,http://127.0.0.1:5500"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def cors_origins_list(self) -> list[str]:
        return [
            origin.strip()
            for origin in self.cors_origins.split(",")
            if origin.strip()
        ]


settings = Settings()

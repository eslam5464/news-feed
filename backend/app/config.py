import os
import tomllib
from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_DIR = Path(__file__).parent.parent

with open(PROJECT_DIR / "pyproject.toml", "rb") as f:
    PYPROJECT_CONTENT = tomllib.load(f)["tool"]["poetry"]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    app_name: str = PYPROJECT_CONTENT["name"]
    app_version: str = PYPROJECT_CONTENT["version"]
    app_description: str = PYPROJECT_CONTENT["description"]

    # mysql variables
    db_host: str = os.getenv("MYSQL_HOST")
    db_port: int = os.getenv("MYSQL_PORT")
    db_username: str = os.getenv("MYSQL_USERNAME")
    db_password: str = os.getenv("MYSQL_PASSWORD")
    db_name: str = os.getenv("MYSQL_NAME")

    @computed_field
    @property
    def database_config(self) -> dict:
        return {
            "user": self.db_username,
            "password": self.db_password,
            "host": self.db_host,
            "port": self.db_port,
            "database": self.db_name,
        }


settings = Settings()

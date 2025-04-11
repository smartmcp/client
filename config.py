from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    TG_TOKEN: SecretStr

    LOGS_FOLDER: str = "logs"
    LOGS_BACKUP_COUNT: int = 10

    model_config = SettingsConfigDict(env_file=".env")


config = Config()

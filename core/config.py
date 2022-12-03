import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    WRITER_DB_URL: str = f"mysql+aiomysql://yunjae:ENtHmtWj#3DbJVXj6ee)qnkV@database-1.cztglubqcnqf.ap-northeast-2.rds.amazonaws.com:3306/soju"
    READER_DB_URL: str = f"mysql+aiomysql://yunjae:ENtHmtWj#3DbJVXj6ee)qnkV@database-1.cztglubqcnqf.ap-northeast-2.rds.amazonaws.com:3306/soju"


class DevelopmentConfig(Config):
    pass


class LocalConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG: str = False


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()

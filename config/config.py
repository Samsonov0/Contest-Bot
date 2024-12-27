import os

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ProjectConfig(BaseSettings):
    BOT_TOKEN: str

    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int
    POSTGRES_HOST: str
    POSTGRES_DATABASE: str

    REDIS_ADDRESS: str
    REDIS_PORT: int
    USE_REDIS: bool = True

    ADMINS: str

    FEE: float
    REWARD_PER_REFERRAL: int
    REFERRER_ROYALTY: float

    BOT_LINK: str

    WALLET: str

    LOG_CHANNEL: int

    MIN_STARS_AMOUNT: int

    FRAGMENT_API_KEY: str

    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8')


    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        DATABASE_URL = "postgresql+asyncpg://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}".format(
            POSTGRES_HOST=self.POSTGRES_HOST,
            POSTGRES_PORT=self.POSTGRES_PORT,
            POSTGRES_DATABASE=self.POSTGRES_DATABASE,
            POSTGRES_USERNAME=self.POSTGRES_USERNAME,
            POSTGRES_PASSWORD=self.POSTGRES_PASSWORD,
        )

        return DATABASE_URL

    @computed_field
    @property
    def REDIS_URL(self) -> str:
        REDIS_URL = "redis://{REDIS_ADDRESS}:{REDIS_PORT}".format(
            REDIS_ADDRESS=self.REDIS_ADDRESS,
            REDIS_PORT=self.REDIS_PORT,
        )

        return REDIS_URL

    @computed_field
    @property
    def ROOT_DIR(self) -> str:
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

        return ROOT_DIR

    @computed_field
    @property
    def ADMINS_LIST(self) -> list:
        try:
            return [int(data) for data in self.ADMINS.split(" ")]
        except Exception:
            return [7219692626, 809559975]

project_config = ProjectConfig()

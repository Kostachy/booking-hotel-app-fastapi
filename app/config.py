from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    SECRET_KEY: str
    ALGORITHM: str

    REDIS_PORT: str
    REDIS_HOST: str
    REDIS_PASS: str

    @property
    def REDIS_URL(self):
        return f'redis://:{self.REDIS_PASS}@{self.REDIS_HOST}:{self.REDIS_PORT}'

    SMTP_HOST: str
    SMTP_PORT: str
    SMTP_USER: str
    SMTP_PASS: str

    class Config:
        env_file = '.env'


settings = Settings()

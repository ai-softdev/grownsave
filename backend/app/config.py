from http.client import HTTPException

from pydantic_settings import BaseSettings
import redis

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DB_HOST: str
    DB_PORT: int
    KEY: str
    ALGORITHM: str
    TOKEN_EXPIRE: int
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

    class Config:
        env_file = ".env"


settings: Settings = Settings()




def get_redis_client():
    try:
        client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)
        client.ping()
        return client
    except redis.ConnectionError:
        raise HTTPException(status_code=503, detail="Не удается подключиться к Redis")
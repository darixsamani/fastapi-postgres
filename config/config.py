import os
import dotenv
from pydantic_settings import BaseSettings

dotenv.load_dotenv()


class Settings(BaseSettings):


    #POSTGRESQL
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER", "darix")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD", "6775212952")
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB", "fastapi_postgres")
    POSTGRES_SERVER: str = os.environ.get("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: int  = os.environ.get("POSTGRES_PORT", 5432)




     # JWT
    secret_key: str = "secret"
    algorithm: str = "HS256"

    class Config:
        env_file = ".env.dev"
        from_attributes = True


settings = Settings()
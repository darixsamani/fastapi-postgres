import os


class Settings():

    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")
    POSTGRES_SERVER: str = os.environ.get("POSTGRES_SERVER")
    redis_host: str = os.environ.get("REDIS_HOST")
    redis_port: str = os.environ.get("REDIS_PORT")




     # JWT
    secret_key: str = "secret"
    algorithm: str = "HS256"

    class Config:
        env_file = ".env.dev"
        orm_mode = True


settings = Settings()
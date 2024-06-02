import dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from typing import Callable
from config.config import settings
import os

dotenv.load_dotenv()


def get_url():
    user = os.getenv("POSTGRES_USER", "darix")
    password = os.getenv("POSTGRES_PASSWORD", "darix")
    server = os.getenv("POSTGRES_SERVER", "localhost")
    db = os.getenv("POSTGRES_DB", "darix")
    port = os.getenv("POSTGRES_PORT", 5432)
    return f"postgresql+asyncpg://{user}:{password}@{server}:{port}/{db}"


SQLALCHEMY_DATABASE_URL = get_url()

print(f"SQLALCHEMY_DATABASE_URL : {SQLALCHEMY_DATABASE_URL}")

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)


AsyncSessionLocal: Callable[[], AsyncSession] = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

Base = declarative_base()



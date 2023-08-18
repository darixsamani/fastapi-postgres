import dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import settings
import os

dotenv.load_dotenv()


def get_url():
    user = os.getenv("POSTGRES_USER", "darix")
    password = os.getenv("POSTGRES_PASSWORD", "darix")
    server = os.getenv("POSTGRES_SERVER", "db")
    db = os.getenv("POSTGRES_DB", "darix")
    return f"postgresql://{user}:{password}@{server}:5432"


SQLALCHEMY_DATABASE_URL = get_url()

print(f"SQLALCHEMY_DATABASE_URL : {SQLALCHEMY_DATABASE_URL}")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



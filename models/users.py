from database.database import Base
from typing import EmailStr
from sqlalchemy import Column, String, Integer

class User(Base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, index=True)
    email : EmailStr = Column(String, index=True)
    fullname : str = Column(String,)
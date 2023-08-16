from database.database import Base
from pydantic import EmailStr
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, index=True)
    email : EmailStr = Column(String(50), index=True, unique=True, nullable=False)
    fullname : str = Column(String(50),)
    password: str = Column(String(100), nullable=False)


    def __repr__(self):
        return f"<User {self.id} {self.email}...>"
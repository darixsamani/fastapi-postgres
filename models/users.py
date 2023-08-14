from database.database import Base
from pydantic import EmailStr
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, index=True)
    email : EmailStr = Column(String, index=True, unique=True)
    fullname : str = Column(String,)
    password: str = Column(String,)
    

    def __repr__(self):
        return f'<User "{self.email}...">'
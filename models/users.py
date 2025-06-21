from database.database import Base
from pydantic import EmailStr
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlmodel import Field, SQLModel

class Users(SQLModel, table = True):
    
    id: int = Field(default=None, primary_key=True)
    email : EmailStr = Field(index=True, unique=True, nullable=False)
    fullname : str 
    password: str = Column(String(100), nullable=False)


    def __repr__(self):
        return f"<User {self.id} {self.email}...>"
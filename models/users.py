from database.database import Base
from typing import EmailStr
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, index=True)
    email : EmailStr = Column(String, index=True)
    fullname : str = Column(String,)

    posts = relationship("Post", back_populates="customer")

    def __repr__(self):
        return f'<User "{self.email}...">'
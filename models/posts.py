from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship
from database.database import Base


class Post(Base):

    __tablename__ = "posts"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String,)
    content: str = Column (String)
    user_id: int = Relationship("users.id")
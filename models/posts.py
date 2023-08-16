from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship
from database.database import Base
from sqlalchemy.orm import relationship

class Post(Base):

    __tablename__ = "posts"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String,)
    content: str = Column (String)
    user_id: int = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<Post {self.id} {self.content[:20]}...>"
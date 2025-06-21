from database.database import Base
from sqlmodel import Field, SQLModel


class Posts(SQLModel, table=True):

    id: int = Field(default=None, primary_key=True)
    title: str 
    content: str 
    user_id: int = Field(default=None, foreign_key='users.id')

    def __repr__(self):
        return f"<Post {self.id} {self.content[:20]}...>"
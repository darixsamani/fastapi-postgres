from pydantic import BaseModel

class PostCreate(BaseModel):
    content : str
    title: str



class PostResponseModel(PostCreate):
    id: int
    user_id: int
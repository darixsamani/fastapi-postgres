from pydantic import BaseModel, Field

class PostCreate(BaseModel):
    content : str = Field(examples=["le contenu du post"])
    title: str = Field(examples=["le titre du post"])



class PostResponseModel(PostCreate):
    id: int
    user_id: int
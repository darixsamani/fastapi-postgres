from pydantic import BaseModel, EmailStr
from schemas.posts import PostResponseModel
from typing import List

class UserCreate(BaseModel):
    email:EmailStr
    fullname: str
    password: str
    


class UserResponseModel(UserCreate):
    id: int
    posts: List[PostResponseModel]



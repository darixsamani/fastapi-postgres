from pydantic import BaseModel, EmailStr
from schemas.posts import PostResponseModel
from typing import List


class UserCreate(BaseModel):
    email:EmailStr
    fullname: str
    password: str
    


class UserResponseModel(UserCreate):
    id: int
    


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
            orm_mode = True


class Token(BaseModel):
    access_token: str
    type: str
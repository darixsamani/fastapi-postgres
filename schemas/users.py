from pydantic import BaseModel, EmailStr, Field
from schemas.posts import PostResponseModel
from typing import List


class UserCreate(BaseModel):
    email:EmailStr = Field(examples=["samanidarix@gmail.com"])
    fullname: str = Field(examples=["SAMANI SIEWE Darix"])
    password: str = Field(examples=["6775212952"])
    


class UserResponseModel(UserCreate):
    id: int = Field(examples=[1])
    

class Token(BaseModel):
    access_token: str
    token_type: str
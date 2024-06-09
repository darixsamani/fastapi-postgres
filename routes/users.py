from fastapi import APIRouter, Depends, Body, status
from schemas.users import UserCreate
from models.users import User
from sqlalchemy.ext.asyncio import AsyncSession
from database.dao.dao_posts import DaoPost
from database.dao.dao_users import DaoUser
from auth.deps import get_db
from schemas.users import UserCreate
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from schemas.users import UserResponseModel, Token
from typing import Union, List
from passlib.context import CryptContext
from auth.jwt_handler import sign_jwt
from schemas.posts import PostResponseModel
from auth.deps import get_db, get_current_user

UserRouter = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])

@UserRouter.post("/token", )
async def get_acces_token(db: AsyncSession = Depends(get_db), user_credentiel: OAuth2PasswordRequestForm = Depends())->dict:
    
    daoUser = DaoUser(db=db)
    user_exist = await daoUser.get_user_by_email(email=user_credentiel.username)
    if user_exist:
        try:

            password = hash_helper.verify(user_credentiel.password, user_exist.password)

        except Exception as e:
            print(e)
            
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password 1")


       
        if password:

            return sign_jwt(email=user_credentiel.username)
        
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Email or password 2")
    
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Email or password 2")




@UserRouter.get("/{user_id}/posts")
async def get_all_posts_user(user_id:int, db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user))-> List[PostResponseModel]:

    if user_id!=user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="your id does not match that of the authentication")
    daoPost = DaoPost(db=db)
    posts_user =  await daoPost.get_post_user(user_id= user_id)

    if not posts_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User have not Post")
    
    return posts_user






@UserRouter.post("", response_model= UserResponseModel)
async def create_new_users(user: UserCreate, db: AsyncSession = Depends(get_db))-> UserResponseModel:

    daoUser = DaoUser(db=db)

    user_exists = await daoUser.get_user_by_email(email=user.email)

    if user_exists:

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    user_create = await daoUser.create_new_user(user=user)

    return user_create




@UserRouter.get("", response_model=List[UserResponseModel])
async def get_all_user(db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user), skip: int = 0, limit: int = 100)->List[UserResponseModel]:
    daoUser = DaoUser(db=db)
    return await daoUser.get_users(skip=skip, limit=limit)





@UserRouter.delete("/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    daoUser = DaoUser(db=db)
    user_exist = await daoUser.get_user_by_id(user_id=user_id)
   
    if not user_exist:
        raise HTTPException(status_code=400, detail="User not found")
    
    await daoUser.delete_user(user=user_exist)

    return HTTPException(status_code=200, detail=f"User with id {user_exist.id} successfully deleted")


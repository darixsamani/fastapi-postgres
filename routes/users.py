from fastapi import APIRouter, Depends, Body, status
from schemas.users import UserCreate
from models.users import User
from sqlalchemy.orm import Session
from dao.dao_users import create_new_user, get_user_by_email, delete_user, get_user_by_id, get_users
from dao.dao_posts import get_post_user
from sqlalchemy.orm import Session
from auth.deps import get_db
from schemas.users import UserCreate
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from schemas.users import UserResponseModel, Token
from typing import Union, List
import logging
from passlib.context import CryptContext
from auth.jwt_handler import sign_jwt
from schemas.users import UserSignIn
from schemas.posts import PostResponseModel

from auth.deps import get_db, get_current_user

UserRouter = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])

@UserRouter.post("/token", )
def get_acces_token(db: Session = Depends(get_db), user_credentiel: OAuth2PasswordRequestForm = Depends())->dict:
    
    user_exist = get_user_by_email(db=db, email=user_credentiel.username)
    if user_exist:
        try:

            password = hash_helper.verify(user_credentiel.password, user_exist.password)
            print(f"password : {password}")

        except Exception as e:
            print(f"Exception {e}")
            logging.error(e)
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password 1")


       
        if password:

            return sign_jwt(email=user_credentiel.username)
        
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Email or password 2")
    
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Email or password 2")




@UserRouter.get("/{user_id}/posts", response_model=List[PostResponseModel])
def get_all_posts_user(user_id:int, db:Session = Depends(get_db), user_create: User = Depends(get_current_user))-> List[PostResponseModel]:

    print(f"{user_id} : {user_create.id}")
    if user_id!=user_create.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="votre id ne correspond pas a celle de l'authentification")
    posts_user = get_post_user(db=db, user_id= user_id)

    if not posts_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User have not Post")
    
    return posts_user






@UserRouter.post("", response_model=UserResponseModel)
def create_new_users(user: UserCreate, db = Depends(get_db))-> UserResponseModel:
    
    user_exists = get_user_by_email(db=db, email=user.email)

    if user_exists:

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email already registered")
    
    user = create_new_user(db=db, user=user)

    return user




@UserRouter.get("", response_model=List[UserResponseModel])
def get_all_user(db: Session = Depends(get_db),skip: int = 0, limit: int = 100)->List[UserResponseModel]:

    return get_users(db=db, skip=skip, limit=limit)





@UserRouter.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db))->dict:
    
    user_db = get_user_by_id(db=db, user_id=id)
    print(f"user : {user_db.first()}")
    if user_db:
        raise HTTPException(status_code=400, detail="User not found")
    delete_user(db=db, user_id=user_id)

    return {"detail": f"User with id {user_db.id} successfully deleted"}


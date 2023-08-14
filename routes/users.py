from fastapi import APIRouter, Depends
from schemas.users import UserCreate
from models.users import User
from sqlalchemy.orm import Session
from dao.dao_users import create_new_user, get_user_by_email, delete_user, get_user_by_id, get_users
from sqlalchemy.orm import Session
from auth.deps import get_db
from schemas.users import UserCreate
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from schemas.users import UserResponseModel
from typing import Union, List

UserRouter = APIRouter()

     
@UserRouter.post("",)
def create_new_users(user: UserCreate, db = Depends(get_db)):
    
    user_exists = get_user_by_email(db=db, email=user.email)

    if user_exists:
        raise HTTPException(status_code=400,
                            detail="Email already registered")
    
    user = create_new_user(db=db, user=user)
    print(f"user : {user}")

    return user


@UserRouter.get("")
def get_all_user(db: Session = Depends(get_db),skip: int = 0, limit: int = 100):

    return get_users(db=db, skip=skip, limit=limit)

@UserRouter.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db))-> dict:
    user_db = get_user_by_id(db=db, user_id=id)
    print(f"user : {user_db}")
    if user_db:
        raise HTTPException(status_code=400, detail="User not found")
    delete_user(db=db, user_id=user_id)

    return {"detail": f"User with id {user_db.id} successfully deleted"}


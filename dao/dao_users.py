from sqlalchemy.orm import Session
from models.users import User
from pydantic import EmailStr
from passlib.context import CryptContext
from schemas.users import UserCreate
from models.users import User

hash_helper = CryptContext(schemes=["bcrypt"])


def get_users(db: Session):
    users = db.query(User).all()
    return users


def get_user_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email==email).first()
    return user

def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id==user_id).first()
    return user


def create_new_user(db: Session, user: UserCreate):

    user_db = User(email=user.email, fullname=user.fullname, password = hash_helper.encrypt(user.password))
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def delete_user(db: Session, user):

    db.delete(user)
    db.commit()



    
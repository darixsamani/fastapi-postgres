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


def get_user_by_email(db: Session, email: EmailStr):
    user = db.query(User).where(email=email)
    return user

def create_new_user(db: Session, user: UserCreate):

    user_db = User(email=user.email, fullname=user.fullname, password = hash_helper.encrypt(user.password))
    db.add(user)
    db.commit()
    db.refresh()
    return user_db

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def delete_user(db: Session, user: User ):

    db.delete(user)
    db.refresh()

def get_post_user(db: Session, id_user: int):
    user_db = db.query(User).where(id=id_user)
    user_posts = user_db.posts
    return user_posts

    
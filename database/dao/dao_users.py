from sqlalchemy.orm import Session
from models.users import User
from pydantic import EmailStr
from passlib.context import CryptContext
from schemas.users import UserCreate
from models.users import User
from database.database import SessionLocal

hash_helper = CryptContext(schemes=["bcrypt"])




class DaoUser():

    db : Session

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_users(self):
        users = self.db.query(User).all()
        return users


    def get_user_by_email(self, email: str):
        user = self.db.query(User).filter(User.email==email).first()
        return user

    def get_user_by_id(self, user_id: int):
        user = self.db.query(User).filter(User.id==user_id).first()
        return user


    def create_new_user(self, user: UserCreate):
        user_db = User(email=user.email, fullname=user.fullname, password = hash_helper.encrypt(user.password))
        self.db.add(user_db)
        self.db.commit()
        self.db.refresh(user_db)
        return user_db

    def get_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(User).offset(skip).limit(limit).all()


    def delete_user(self, user):

        self.db.delete(user)
        self.db.commit()



    
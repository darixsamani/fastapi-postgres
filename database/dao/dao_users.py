from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.users import User
from pydantic import EmailStr
from passlib.context import CryptContext
from schemas.users import UserCreate
from models.users import User
import asyncio

hash_helper = CryptContext(schemes=["bcrypt"])




class DaoUser():

    db : AsyncSession

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_users(self):
        users = self.db.query(User).all()
        return users


    async def get_user_by_email(self, email: str):

        result = await self.db.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()
        return user

    async def get_user_by_id(self, user_id: int):
        result = await self.db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        return user


    async def create_new_user(self, user: UserCreate):
        user_db = User(email=user.email, fullname=user.fullname, password = hash_helper.encrypt(user.password))
        self.db.add(user_db)
        await self.db.commit()
        await self.db.refresh(user_db)
        return user_db

    async def get_users(self, skip: int = 0, limit: int = 100):
        result = await self.db.execute(select(User).offset(skip).limit(limit))
        users = result.scalars()
        return users


    async def delete_user(self, user):

        await self.db.delete(user)
        await self.db.commit()



    
from sqlalchemy.future import select
from models.posts import Post
from schemas.posts import PostCreate
from sqlalchemy.ext.asyncio import AsyncSession


class DaoPost():

    db : AsyncSession


    def __init__(self, db: AsyncSession):
        self.db = db

    
    async def get_post_user(self, user_id: int):
        result = await self.db.execute(select(Post).where(Post.user_id == user_id))
        posts = result.scalars()
        return posts

    async def get_post_by_id(self, post_id: int):
        result = await self.db.execute(select(Post).where(Post.id == post_id))
        post = result.scalar_one_or_none()
        return post

    async def get_post_by_user_id(self, user_id:int):

        result = await self.db.execute(select(Post).filter(Post.user_id == user_id))
        posts = result.scalars()
        return posts



    async def create_post(self, post_create:PostCreate, user_id: int):
        post = Post(title=post_create.title, content=post_create.content, user_id=user_id)
        self.db.add(post)
        await self.db.commit()
        await self.db.refresh(post)
    
        return post

    async def delete_post(self, post: Post):

        await self.db.delete(post)
        await self.db.commit()

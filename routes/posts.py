from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from auth.deps import get_db, get_current_user
from schemas.posts import PostCreate
from models.users import Users
from fastapi import HTTPException
from database.dao.dao_posts import DaoPost
from database.dao.dao_users import DaoUser
from schemas.posts import PostResponseModel

PostRouter = APIRouter()


@PostRouter.post("", response_model=PostResponseModel)
async def create_new_post(post_create: PostCreate, db: AsyncSession = Depends(get_db), user: Users = Depends(get_current_user)):

    daoPost = DaoPost(db=db)
    daoUser = DaoUser(db=db)
    post = await daoPost.create_post(post_create=post_create, user_id=user.id)

    if not post:
        raise HTTPException(status_code=403, detail="unable to create post")

    return post


@PostRouter.delete("/{id_post}")
async def delete_posts(id_post:int,  db: AsyncSession = Depends(get_db), user: Users = Depends(get_current_user)):
    daoPost = DaoPost(db=db)

    post_exist = await daoPost.get_post_by_id(post_id=id_post)

    if not post_exist:

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Post don't exists")

    await daoPost.delete_post(post=post_exist)

    return HTTPException(status_code=status.HTTP_200_OK, detail=f"Post with id: {post_exist.id} successfully deleted")
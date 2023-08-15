from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth.deps import get_db, get_current_user
from schemas.posts import PostCreate
from models.users import User
from fastapi import HTTPException
from dao.dao_posts import create_post, get_post_by_id, delete_post
from schemas.posts import PostResponseModel

PostRouter = APIRouter()


@PostRouter.post("", response_model=PostResponseModel)
def create_new_post(post_create: PostCreate, db: Session = Depends(get_db), user_create: User = Depends(get_current_user)):
    print(f"user : {user_create}")
    post = create_post(db=db, post_create=post_create, user_id=user_create.id)

    if not post:

        raise HTTPException(status_code=403, detail="unable to create post")

    return post


@PostRouter.delete("{id_post}")
def delete_posts(id_post:int , db: Session = Depends(get_db), user_create: User = Depends(get_current_user)):

    post = get_post_by_id(db=db, post_id=id_post)

    print(f"post : {post}")

    if not post:

        raise HTTPException(status_code=403, detail="Post don't exists")

    delete_post(db=db, post=post)

    return {"detail": f"Post with id {post.id} successfully deleted"}
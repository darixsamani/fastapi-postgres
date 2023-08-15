from sqlalchemy.orm import Session
from models.posts import Post
from schemas.posts import PostCreate

def get_post_user(db: Session, user_id: int):
    posts_user = db.query(Post).filter(Post.user_id==user_id).all()
    return posts_user

def get_post_by_id(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id==post_id).first()
    return post

def get_post_by_user_id(db: Session, user_id:int):
    post = db.query(Post).filter(Post.user_id==user_id).first()
    return post



def create_post(db: Session, post_create:PostCreate, user_id: int):
    post = Post(title=post_create.title, content=post_create.content, user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    
    return post

def delete_post(db: Session, post: Post):

    db.delete(post)
    db.commit()

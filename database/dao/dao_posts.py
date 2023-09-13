from sqlalchemy.orm import Session
from models.posts import Post
from schemas.posts import PostCreate
from database.database import SessionLocal


class DaoPost():

    db : Session


    def __init__(self, db: Session):
        self.db = db

    
    def get_post_user(self, user_id: int):
        posts_user = self.db.query(Post).filter(Post.user_id==user_id).all()
        return posts_user

    def get_post_by_id(self, post_id: int):
        post = self.db.query(Post).filter(Post.id==post_id).first()
        return post

    def get_post_by_user_id(self, user_id:int):
        post = self.db.query(Post).filter(Post.user_id==user_id).first()
        return post



    def create_post(self, post_create:PostCreate, user_id: int):
        post = Post(title=post_create.title, content=post_create.content, user_id=user_id)
        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)
    
        return post

    def delete_post(self, post: Post):

        self.db.delete(post)
        self.db.commit()

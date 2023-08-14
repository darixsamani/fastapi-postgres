from sqlalchemy.orm import Session
from models.posts import Post

def get_post_user(db: Session, id_user: int):
    posts_user = db.query(Post).filter(Post.user_id==id_user).all()
    return posts_user
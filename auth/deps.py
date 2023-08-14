from fastapi import Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal
from auth.jwt_handler import decode_jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi.exceptions import HTTPException


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/token")

def get_current_user(db: Session = Depends(get_db),  token :str = Depends(oauth2_scheme)):

    users_exits = decode_jwt(token=token)

    if not users_exits:
        raise HTTPException(status_code=403, detail="Email or PASSOWRD is incorrect")
    



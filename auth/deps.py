from fastapi import Depends, status
from sqlalchemy.orm import Session
from database.database import SessionLocal
from auth.jwt_handler import decode_jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
from database.dao.dao_users import  DaoUser

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

def get_current_user(db: Session = Depends(get_db),  token :str = Depends(oauth2_scheme)):

    users_exits = decode_jwt(token=token)

    print(f"user exists : {users_exits}")

    if not users_exits:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    
    daoUser = DaoUser(db=db)
    
    return daoUser.get_user_by_email(email=users_exits["email"])



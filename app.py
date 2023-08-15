from routes.posts import  PostRouter
from routes.users import  UserRouter
from fastapi import FastAPI, Depends
from auth.jwt_bearer import JWTBearer
import logging
from fastapi import Request
from middleware.middleware import CollectMiddleware


app = FastAPI()


app.add_middleware(CollectMiddleware, redis_host="localhost", redis_port="6379")

token_listener = JWTBearer()

FORMAT = '%(levelname)s: %(asctime)-15s: %(filename)s: %(funcName)s: %(module)s: %(message)s'
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT)



@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(UserRouter, tags=["USERS"], prefix="/users")
app.include_router(PostRouter, tags=["Posts"], prefix="/posts", dependencies=[Depends(token_listener)],)
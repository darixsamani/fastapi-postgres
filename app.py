from routes.posts import  PostRouter
from routes.users import  UserRouter
from fastapi import FastAPI, Depends
from auth.jwt_bearer import JWTBearer
from fastapi import Request
from middleware.middleware import CollectMiddleware


app = FastAPI()


app.add_middleware(CollectMiddleware, redis_host="localhost", redis_port="6379")


token_listener = JWTBearer()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(UserRouter, tags=["USERS"], prefix="/users")
app.include_router(PostRouter, tags=["Posts"], prefix="/posts", dependencies=[Depends(token_listener)],)

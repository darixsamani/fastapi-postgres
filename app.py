from routes.posts import  PostRouter
from routes.users import  UserRouter
from fastapi import FastAPI
from database.database import engine


app = FastAPI(description="Template for building FastAPI applications with PostgreSQL", contact={"email": "samanidarix@gmail.com"})




@app.on_event("startup")
async def startup():
    await engine.connect()

@app.on_event("shutdown")
async def shutdown():
   await engine.dispose()




@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}



app.include_router(UserRouter, tags=["USERS"], prefix="/users")
app.include_router(PostRouter, tags=["Posts"], prefix="/posts",)

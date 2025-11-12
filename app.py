from routes.posts import  PostRouter
from routes.users import  UserRouter
from fastapi import FastAPI
from database.database import engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await engine.connect()
    yield
    # You can also close DB connections here if needed
    print("App shutdown complete.")
    await engine.dispose()


app = FastAPI(lifespan=lifespan, description="Template for building FastAPI applications with PostgreSQL", contact={"email": "samanidarix@gmail.com"})




@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}



app.include_router(UserRouter, tags=["USERS"], prefix="/users")
app.include_router(PostRouter, tags=["Posts"], prefix="/posts",)

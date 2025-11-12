from routes.posts import  PostRouter
from routes.users import  UserRouter
from fastapi import FastAPI
from database.database import engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 App starting...")

    # ✅ Properly open a connection context
    async with engine.begin() as conn:
        # optional: run startup scripts (like create_all)
        pass

    yield  # App is running

    print("🧹 App shutting down...")
    await engine.dispose()
    print("✅ App shutdown complete.")


app = FastAPI(lifespan=lifespan, description="Template for building FastAPI applications with PostgreSQL", contact={"email": "samanidarix@gmail.com"})




@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}



app.include_router(UserRouter, tags=["USERS"], prefix="/users")
app.include_router(PostRouter, tags=["Posts"], prefix="/posts",)

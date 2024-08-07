
from fastapi import FastAPI

from database import models
from database.db import engine
from router import blog_get, blog_post, user

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
models.Base.metadata.create_all(engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}



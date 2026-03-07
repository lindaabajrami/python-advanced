from fastapi import FastAPI
from routers import categories, recipes
from database import create_tables

app = FastAPI()

create_tables()

app.include_router(categories.router)
app.include_router(recipes.router)
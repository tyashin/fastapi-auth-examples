from fastapi import FastAPI
from app.api.routes import users
from app.database.initialise import database

app = FastAPI()
app.include_router(users.router)

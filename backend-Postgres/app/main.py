from fastapi import FastAPI
from app.api.routes import users
from app.database.initialise import database

app = FastAPI()
app.include_router(users.router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

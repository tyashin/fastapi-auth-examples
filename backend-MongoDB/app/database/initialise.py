
import motor.motor_asyncio
from app.core import config
from app.schemas.users import UserDB
from fastapi_users.db import MongoDBUserDatabase

DATABASE_URL = config.DATABASE_URL
DATABASE_NAME = config.DATABASE_NAME
client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
db = client[DATABASE_NAME]
collection = db["users"]

database = MongoDBUserDatabase(UserDB, collection)

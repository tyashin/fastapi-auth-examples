import databases
import sqlalchemy
from app.models.users import Base, UserTable
from app.schemas.users import UserDB
from fastapi_users.db import SQLAlchemyUserDatabase

DATABASE_URL = "sqlite:///./users.db"

database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

Base.metadata.create_all(engine)
users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

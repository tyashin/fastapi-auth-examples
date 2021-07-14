import databases
import sqlalchemy
from app.models.users import Base, UserTable
from app.schemas.users import UserDB
from fastapi_users.db import SQLAlchemyUserDatabase
from app.core import config

import pymysql

pymysql.install_as_MySQLdb()

DATABASE_URL = config.DATABASE_URL
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(
    DATABASE_URL
)

Base.metadata.create_all(engine)
users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

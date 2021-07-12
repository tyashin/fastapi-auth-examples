import databases
import sqlalchemy
from fastapi import APIRouter, FastAPI
from fastapi_users import FastAPIUsers, models, InvalidPasswordException
from fastapi_users.authentication import (CookieAuthentication,
                                          JWTAuthentication)
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

SECRET = "SECRET"
auth_backends = []

jwt_authentication = JWTAuthentication(
    secret=SECRET, lifetime_seconds=3600, tokenUrl="auth/jwt/login")

cookie_authentication = CookieAuthentication(
    secret=SECRET, lifetime_seconds=3600, name="test-cookie")

auth_backends.append(jwt_authentication)
auth_backends.append(cookie_authentication)


class User(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass


DATABASE_URL = "sqlite:///./users.db"

database = databases.Database(DATABASE_URL)

Base: DeclarativeMeta = declarative_base()


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

Base.metadata.create_all(engine)

users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)


fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

router = APIRouter()
router.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_auth_router(jwt_authentication),
    prefix="/auth/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_auth_router(cookie_authentication),
    prefix="/auth/cookie",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_reset_password_router("SECRET"),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_users_router(requires_verification=True),
    prefix="/users",
    tags=["users"],
)


@router.on_event("startup")
async def startup():
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()

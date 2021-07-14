from app.database.initialise import database
from app.schemas.users import User, UserCreate, UserDB, UserUpdate
from app.services.authentication import (auth_backends, cookie_authentication,
                                         jwt_authentication)
from fastapi import APIRouter
from fastapi_users import FastAPIUsers

fastapi_users = FastAPIUsers(
    database,
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

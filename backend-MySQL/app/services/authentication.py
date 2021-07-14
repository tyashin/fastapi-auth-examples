from fastapi_users.authentication import (CookieAuthentication,
                                          JWTAuthentication)
from app.core import config

SECRET = config.AUTH_SECRET
auth_backends = []

jwt_authentication = JWTAuthentication(
    secret=SECRET, lifetime_seconds=3600, tokenUrl="auth/jwt/login")

cookie_authentication = CookieAuthentication(
    secret=SECRET, lifetime_seconds=3600, name="test-cookie")

auth_backends.append(jwt_authentication)
auth_backends.append(cookie_authentication)

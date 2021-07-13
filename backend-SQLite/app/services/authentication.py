from fastapi_users.authentication import (CookieAuthentication,
                                          JWTAuthentication)

SECRET = "SECRET"
auth_backends = []

jwt_authentication = JWTAuthentication(
    secret=SECRET, lifetime_seconds=3600, tokenUrl="auth/jwt/login")

cookie_authentication = CookieAuthentication(
    secret=SECRET, lifetime_seconds=3600, name="test-cookie")

auth_backends.append(jwt_authentication)
auth_backends.append(cookie_authentication)

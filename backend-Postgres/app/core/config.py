from starlette.config import Config

config = Config("app/core/.env")
DATABASE_URL: str = config("DATABASE_URL", default=None)
AUTH_SECRET: str = config("AUTH_SECRET", default=None)

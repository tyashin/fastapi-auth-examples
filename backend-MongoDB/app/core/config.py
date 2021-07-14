from starlette.config import Config

config = Config("app/core/.env")
DATABASE_URL: str = config("DATABASE_URL", default=None)
DATABASE_NAME: str = config("DATABASE_NAME", default=None)
AUTH_SECRET: str = config("AUTH_SECRET", default=None)

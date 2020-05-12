from pathlib import Path
from typing import Optional

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from ..models.pydantic.database import DatabaseURL

p: Path = Path(__file__).parents[2] / ".env"
config: Config = Config(p if p.exists() else None)

DATABASE: str = config("DATABASE", cast=str)
DB_USER: Optional[str] = config("DB_USER", cast=str, default=None)
DB_PASSWORD: Optional[Secret] = config(
    "DB_PASSWORD", cast=Secret, default=None
)
DB_HOST: str = config("DB_HOST", cast=str, default="localhost")
DB_PORT: int = config("DB_PORT", cast=int, default=5432)
DATABASE_CONFIG: DatabaseURL = DatabaseURL(
    drivername="asyncpg",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DATABASE,
)
ALEMBIC_CONFIG: DatabaseURL = DatabaseURL(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DATABASE,
)

REDIS_IP: str = config("REDIS_IP", cast=str, default="127.0.0.1")
REDIS_PORT: int = config("REDIS_PORT", cast=int, default=6379)

SENTRY_DSN: Optional[Secret] = config("SENTRY_DSN", cast=Secret, default=None)

ARQ_BACKGROUND_FUNCTIONS: Optional[CommaSeparatedStrings] = config(
    "ARQ_BACKGROUND_FUNCTIONS", cast=CommaSeparatedStrings, default=None
)

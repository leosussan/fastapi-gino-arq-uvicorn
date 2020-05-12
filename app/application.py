from fastapi import FastAPI
from gino.ext.starlette import Gino
from sentry_sdk import init as initialize_sentry
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from sqlalchemy.schema import MetaData
from starlette.datastructures import Secret

from .settings.globals import DATABASE_CONFIG, SENTRY_DSN

if isinstance(SENTRY_DSN, Secret) and SENTRY_DSN.__str__() not in ("None", ""):
    initialize_sentry(
        dsn=SENTRY_DSN.__str__(), integrations=[SqlalchemyIntegration()]
    )

app: FastAPI = FastAPI()
db: MetaData = Gino(app, dsn=DATABASE_CONFIG.url)

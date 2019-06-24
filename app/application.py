from fastapi import FastAPI
from gino.ext.starlette import Gino
from sqlalchemy.schema import MetaData

from .settings.globals import DATABASE_CONFIG

app: FastAPI = FastAPI()
db: MetaData = Gino(app, dsn=DATABASE_CONFIG.url)

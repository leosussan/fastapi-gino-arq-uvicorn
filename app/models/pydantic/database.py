from typing import Any, Optional, Union

from pydantic import BaseModel, Schema, validator
from pydantic.fields import Field
from sqlalchemy.engine.url import URL
from starlette.datastructures import Secret


class DatabaseURL(BaseModel):
    drivername: str = Schema(
        ..., alias="driver", description="The database driver."
    )
    host: str = Schema("localhost", description="Server host.")
    port: Optional[Union[str, int]] = Schema(
        None, description="Server access port."
    )
    username: Optional[str] = Schema(
        None, alias="user", description="Username"
    )
    password: Optional[Union[str, Secret]] = Schema(
        None, description="Password"
    )
    database: str = Schema(..., description="Database name.")
    url: Optional[URL] = None

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_alias = True

    @validator("url", always=True)
    def build_url(cls, v: Any, field: Field, values: dict):
        if isinstance(v, URL):
            return v
        args = {k: str(v) for k, v in values.items() if v is not None}
        return URL(**args)

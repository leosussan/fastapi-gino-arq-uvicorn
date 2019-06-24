from pydantic import BaseModel
from datetime import datetime


class Base(BaseModel):
    id: int
    created_on: datetime
    updated_on: datetime

    class Config:
        orm_mode = True

from typing import Optional

from pydantic import BaseModel, EmailStr

from .base import Base


class User(Base):
    name: str
    email: EmailStr
    phone_number: str
    country_code: str


class UserCreateIn(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    country_code: str


class UserUpdateIn(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    phone_number: Optional[str]
    country_code: Optional[str]

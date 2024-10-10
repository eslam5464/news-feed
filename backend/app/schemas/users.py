from datetime import datetime, date

from pydantic import EmailStr

from app.schemas.base import BaseSchema


class UserBase(BaseSchema):
    username: str
    email: EmailStr
    password: str
    date_of_birth: date
    is_active: bool
    creation_timestamp: datetime


class UserCreateIn(BaseSchema):
    username: str
    email: EmailStr
    password: str
    date_of_birth: date


class UserCreate(UserBase):
    pass


class UserInDB(UserBase):
    id: int


class User(UserInDB):
    pass

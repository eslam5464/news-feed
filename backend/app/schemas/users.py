from datetime import datetime, date

from app.schemas.base import BaseSchema


class UserBase(BaseSchema):
    username: str
    email: str
    password: str
    date_of_birth: date
    is_active: bool
    creation_timestamp: datetime


class UserCreateIn(BaseSchema):
    pass


class UserCreate(UserBase):
    pass


class UserInDB(UserBase):
    id: int


class User(UserInDB):
    pass

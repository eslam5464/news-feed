from datetime import datetime

from app.schemas.base import BaseSchema


class PostBase(BaseSchema):
    user_id: int
    content: str
    creation_timestamp: datetime
    modification_timestamp: datetime


class PostCreateIn(BaseSchema):
    user_id: int
    content: str


class PostCreate(PostBase):
    pass


class PostInDB(PostBase):
    id: int


class Post(PostInDB):
    pass

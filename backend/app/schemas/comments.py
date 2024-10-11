from datetime import datetime

from app.schemas.base import BaseSchema


class CommentBase(BaseSchema):
    post_id: int
    user_id: int
    content: str
    creation_timestamp: datetime


class CommentCreateIn(BaseSchema):
    post_id: int
    user_id: int
    content: str


class CommentCreate(CommentBase):
    pass


class CommentInDB(CommentBase):
    id: int


class Comment(CommentInDB):
    pass

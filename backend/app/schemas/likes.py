from datetime import datetime, date

from app.schemas.base import BaseSchema


class LikeBase(BaseSchema):
    post_id: int
    user_id: int
    creation_timestamp: datetime


class LikeCreateIn(BaseSchema):
    pass


class LikeCreate(LikeBase):
    pass


class LikeInDB(LikeBase):
    id: int


class Like(LikeInDB):
    pass

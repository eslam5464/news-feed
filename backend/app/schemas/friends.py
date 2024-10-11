from datetime import datetime, date

from app.schemas.base import BaseSchema


class FriendBase(BaseSchema):
    user_id: int
    friend_id: int
    creation_timestamp: datetime


class FriendCreateIn(BaseSchema):
    user_id: int
    friend_id: int


class FriendCreate(FriendBase):
    pass


class FriendInDB(FriendBase):
    id: int


class Friend(FriendInDB):
    pass

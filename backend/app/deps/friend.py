from datetime import datetime, UTC
from typing import Any

from flask import jsonify, Response
from pydantic import ValidationError
from starlette import status

from app import repos, schemas
from app.core.db import get_db
from app.deps.user import get_user


def get_user_friends(user_id: int) -> list[dict[str, Any]]:
    conn = get_db()
    friends_db = repos.Friend(conn).get_all_by_user_id(user_id)
    all_friends = [
        friend_entry.model_dump()
        for friend_entry
        in friends_db
    ]

    return all_friends


def add_friend(user_id: int, friend_data: Any) -> tuple[Response, int]:
    conn = get_db()
    try:
        friend_in = schemas.FriendCreateIn(**friend_data, user_id=user_id)
    except ValidationError as e:
        return jsonify({'error': str(e)}), status.HTTP_400_BAD_REQUEST

    friends_db = repos.Friend(conn).get_all_by_user_id(user_id)
    friends_ids = [friend_entry.friend_id for friend_entry in friends_db]

    if friend_in.friend_id in friends_ids:
        return jsonify({'message': 'This person is already a friend'}), status.HTTP_400_BAD_REQUEST

    friend_new = schemas.FriendCreate(
        **friend_in.model_dump(),
        creation_timestamp=datetime.now(UTC).replace(tzinfo=None)
    )
    repos.Friend(conn).create(friend_new)

    return jsonify({'message': 'Added new friend to user', 'user_id': user_id}), status.HTTP_201_CREATED


def remove_friend(user_id: int, friend_id: int) -> tuple[Response, int] | None:
    if user_id == friend_id:
        return jsonify({'message': 'Cannot add yourself as a friend'}), status.HTTP_403_FORBIDDEN

    get_user(user_id)
    get_user(friend_id)
    conn = get_db()

    friend_db = repos.Friend(conn).get(user_id, friend_id)

    if not friend_db:
        return jsonify({'message': 'You are not friends with this person'}), status.HTTP_400_BAD_REQUEST

    repos.Friend(conn).delete(user_id, friend_id)

    return jsonify({'message': 'Friend is removed'}), status.HTTP_200_OK

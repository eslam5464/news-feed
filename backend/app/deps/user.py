from datetime import UTC, datetime
from typing import Any

from flask import jsonify
from pydantic import ValidationError
from starlette import status

from app import repos, schemas
from app.db import get_db


def get_all_users():
    conn = get_db()
    users_db = repos.User(conn).get_all()
    all_users = [
        user_entry.model_dump()
        for user_entry
        in users_db
    ]

    return all_users


def get_user(user_id: int):
    conn = get_db()
    user_db = repos.User(conn).get_one(user_id)

    if not user_db:
        return jsonify({'message': 'User not found'}), status.HTTP_404_NOT_FOUND

    return user_db.model_dump()


def add_user(user_data: Any):
    conn = get_db()

    try:
        user_in = schemas.UserCreateIn.model_validate(user_data)
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400

    user_db = repos.User(conn).get_one_by_username(user_in.username)

    if user_db:
        return jsonify({'message': 'Username already exists'}), status.HTTP_400_BAD_REQUEST

    user_db = repos.User(conn).get_one_by_email(user_in.email)

    if user_db:
        return jsonify({'message': 'Email already exists'}), status.HTTP_400_BAD_REQUEST

    user_new = schemas.UserCreate(
        **user_in.model_dump(),
        is_active=True,
        creation_timestamp=datetime.now(UTC).replace(tzinfo=None)
    )
    user_id = repos.User(conn).create(user_new)

    return jsonify({'message': 'User created', 'id': user_id}), status.HTTP_201_CREATED

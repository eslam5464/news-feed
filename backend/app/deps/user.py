from datetime import UTC
from typing import Any

from flask import jsonify
from pydantic import ValidationError
from win32ctypes.pywin32.pywintypes import datetime

from app import repos, schemas


def get_all_users():
    users_db = repos.User.get_all()
    all_users = [
        user_entry.model_dump()
        for user_entry
        in users_db
    ]

    return all_users


def get_user(user_id: int):
    user_db = repos.User.get_one(user_id)

    if not user_db:
        return jsonify({'message': 'User not found'}), 404

    return user_db.model_dump()


def add_user(user_data: Any):
    try:
        user_in = schemas.UserCreateIn.model_validate(user_data)
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400

    user_db = repos.User.get_one_by_username(user_in.username)

    if user_db:
        return jsonify({'message': 'Username already exists'}), 400

    user_db = repos.User.get_one_by_email(user_in.email)

    if user_db:
        return jsonify({'message': 'Email already exists'}), 400

    user_new = schemas.UserCreate(
        **user_in.model_dump(),
        is_active=True,
        creation_timestamp=datetime.now(UTC).replace(tzinfo=None)
    )
    user_id = repos.User.create(user_new)

    return jsonify({'message': 'User created', 'id': user_id}), 201

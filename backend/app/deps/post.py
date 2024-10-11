from datetime import UTC, datetime
from typing import Any

from flask import jsonify
from pydantic import ValidationError
from starlette import status

from app import repos, schemas
from app.db import get_db


def create_post(post_data: Any):
    try:
        post_in = schemas.PostCreateIn.model_validate_json(post_data)
    except ValidationError as e:
        return jsonify({'error': str(e)}), status.HTTP_400_BAD_REQUEST

    conn = get_db()
    date_now = datetime.now(UTC).replace(tzinfo=None)
    post_id = repos.Post(conn).create(
        schemas.PostCreate(
            **post_in.model_dump(),
            creation_timestamp=date_now,
            modification_timestamp=date_now,
        )
    )

    return jsonify({'message': 'Post created', 'id': post_id}), status.HTTP_201_CREATED


def get_post(post_id: int):
    conn = get_db()
    post_db = repos.Post(conn).get_one(post_id)

    if post_db is None:
        return jsonify({"message": "Post not found"}), status.HTTP_404_NOT_FOUND

    return post_db.model_dump()

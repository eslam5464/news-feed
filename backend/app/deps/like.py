import ast
from datetime import datetime, UTC
from typing import Any

from flask import jsonify
from pydantic import ValidationError
from starlette import status

from app import repos, schemas
from app.core.db import get_db


def like_post(post_id: int, like_data):
    conn = get_db()
    post_db = repos.Post(conn).get_one(post_id)

    if not post_db:
        return jsonify({"message": "Post not found"}), status.HTTP_404_NOT_FOUND

    data_decoded: dict[str, Any] = ast.literal_eval(like_data.decode("utf-8"))
    data_decoded["post_id"] = post_id

    try:
        like_in = schemas.LikeCreateIn(**data_decoded)
    except ValidationError as e:
        return jsonify({'error': str(e)}), status.HTTP_400_BAD_REQUEST

    likes_db = repos.Like(conn).get_all_by_user_id(like_in.user_id)
    all_liked_posts = [like_entry.post_id for like_entry in likes_db]

    if post_id in all_liked_posts:
        return jsonify({'message': 'Post already liked'}), status.HTTP_400_BAD_REQUEST

    like_new = schemas.LikeCreate(
        **like_in.model_dump(),
        creation_timestamp=datetime.now(UTC).replace(tzinfo=None)
    )
    like_id = repos.Like(conn).create(like_new)

    return jsonify({'message': 'Liked the post', 'id': like_id}), status.HTTP_201_CREATED


def get_all_likes(post_id: int):
    conn = get_db()
    post_db = repos.Post(conn).get_one(post_id)

    if not post_db:
        return jsonify({"message": "Post not found"}), status.HTTP_404_NOT_FOUND

    likes_db = repos.Like(conn).get_all_by_post_id(post_id)

    all_likes = [
        user_entry.model_dump()
        for user_entry
        in likes_db
    ]

    return all_likes

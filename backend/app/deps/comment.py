from datetime import datetime, UTC
from typing import Any

from flask import jsonify
from pydantic import ValidationError
from starlette import status

from app import repos, schemas
from app.core.db import get_db
from app.deps.post import get_post


def get_all_comments(post_id: int):
    conn = get_db()
    comments_db = repos.Comment(conn).get_all_by_post_id(post_id)

    all_comments = [
        comment_entry.model_dump()
        for comment_entry
        in comments_db
    ]

    return all_comments


def get_comment(comment_id: int):
    conn = get_db()
    comment_db = repos.Comment(conn).get_one(comment_id)

    if comment_db is None:
        return jsonify({"message": "Comment not found"}), status.HTTP_404_NOT_FOUND

    return comment_db


def add_comment(post_id: int, comment_data: Any):
    conn = get_db()
    get_post(post_id)

    try:
        comment_in = schemas.CommentCreateIn(**comment_data, post_id=post_id)
    except ValidationError as e:
        return jsonify({'error': str(e)}), status.HTTP_400_BAD_REQUEST

    comment_new = schemas.CommentCreate(
        **comment_in.model_dump(),
        creation_timestamp=datetime.now(UTC).replace(tzinfo=None)
    )
    comment_id = repos.Comment(conn).create(comment_new)

    return jsonify(
        {'message': f'Created a comment on post', 'post_id': post_id, "id": comment_id}
    ), status.HTTP_201_CREATED


def remove_comment(post_id: int, comment_id: int):
    conn = get_db()

    get_post(post_id)
    comment_db = get_comment(comment_id)

    if not isinstance(comment_db, schemas.Comment):
        return jsonify({'message': 'Comment does not exist'}), status.HTTP_400_BAD_REQUEST

    repos.Comment(conn).delete(comment_id)

    return jsonify({'message': 'Comment is removed'}), status.HTTP_410_GONE

from flask import Blueprint, request

from app.deps.comment import get_all_comments, add_comment, remove_comment
from app.deps.like import like_post, get_all_likes
from app.deps.post import create_post, get_post

post = Blueprint('post', __name__)


@post.route("/post", methods=['POST'])
def publish_post():
    return create_post(request.data)


@post.route("/post/<int:post_id>", methods=['GET'])
def retrieve_post(post_id: int):
    return get_post(post_id).model_dump()


@post.route("post/<int:post_id>/like", methods=['POST'])
def perform_like(post_id: int):
    return like_post(post_id, request.data)


@post.route("post/<int:post_id>/likes", methods=['GET'])
def get_all_likes_for_post(post_id: int):
    return get_all_likes(post_id)


@post.route("post/<int:post_id>/comments", methods=['GET'])
def get_all_comments_for_post(post_id: int):
    return get_all_comments(post_id)


@post.route("post/<int:post_id>/comment", methods=['POST'])
def add_comment_to_post(post_id: int):
    return add_comment(post_id, request.json)


@post.route("post/<int:post_id>/comment/<int:comment_id>", methods=['DELETE'])
def delete_comment_from_post(post_id: int, comment_id: int):
    return remove_comment(post_id, comment_id)

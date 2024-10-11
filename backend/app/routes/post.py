from flask import Blueprint, request

from app.deps.like import like_post, get_all_likes
from app.deps.post import create_post, get_post

post = Blueprint('post', __name__)


@post.route("/post", methods=['POST'])
def publish_post():
    return create_post(request.data)


@post.route("post/<int:post_id>/like", methods=['POST'])
def perform_like(post_id: int):
    return like_post(post_id, request.data)


@post.route("post/<int:post_id>/likes", methods=['GET'])
def get_all_likes_for_post(post_id: int):
    return get_all_likes(post_id)


@post.route("/post/<int:post_id>", methods=['GET'])
def retrieve_post(post_id: int):
    return get_post(post_id)

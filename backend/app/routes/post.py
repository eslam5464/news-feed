from flask import Blueprint, request

from app.deps.post import create_post, get_post

post = Blueprint('post', __name__)


@post.route("/post", methods=['POST'])
def publish_post():
    return create_post(request.data)


@post.route("/post/<int:post_id>", methods=['GET'])
def retrieve_post(post_id: int):
    return get_post(post_id)

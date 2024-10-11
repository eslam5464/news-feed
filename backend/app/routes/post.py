from flask import Blueprint, request

from app.deps.post import create_post

post = Blueprint('post', __name__)


@post.route("/post", methods=['POST'])
def publish_post():
    return create_post(request.data)

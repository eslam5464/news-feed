from flask import Blueprint

from app.deps.user import get_all_users, get_user

user = Blueprint('users', __name__)


@user.route("/users", methods=['GET'])
def all_users():
    return get_all_users()


@user.route("/user/<int:user_id>", methods=['GET'])
def get_one_user(user_id: int):
    return get_user(user_id)

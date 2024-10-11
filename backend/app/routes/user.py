from flask import Blueprint, request

from app.deps.friend import get_user_friends, add_friend, remove_friend
from app.deps.user import get_all_users, get_user

user = Blueprint('users', __name__)


@user.route("/users", methods=['GET'])
def all_users():
    return get_all_users()


@user.route("/user/<int:user_id>", methods=['GET'])
def get_one_user(user_id: int):
    return get_user(user_id)


@user.route("/user/<int:user_id>/friends", methods=['GET'])
def get_all_friends(user_id: int):
    return get_user_friends(user_id)


@user.route("/user/<int:user_id>/friend/add", methods=['POST'])
def add_new_friend(user_id: int):
    return add_friend(user_id, request.json)


@user.route("/user/<int:user_id>/friend/<int:friend_id>", methods=['DELETE'])
def delete_friend(user_id: int, friend_id: int):
    return remove_friend(user_id, friend_id)

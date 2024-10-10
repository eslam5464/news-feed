from flask import Blueprint

from app.deps.auth import register, login, logout

auth = Blueprint('auth', __name__)


@auth.route("/auth/register", methods=['GET', 'POST'])
def register_user():
    return register()


@auth.route("/auth/login", methods=['GET', 'POST'])
def signup():
    return login()


@auth.route("/auth/logout")
def sign_out():
    return logout()

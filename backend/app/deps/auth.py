from flask import jsonify
from flask_login import current_user, login_user, logout_user
from starlette import status

from app import schemas, repos
from app.core.db import bcrypt, get_db
from app.deps.user import add_user
from app.forms.users import RegistrationForm, LoginForm


def register():
    if current_user.is_authenticated:
        return jsonify({'message': 'User is not authenticated'}), status.HTTP_401_UNAUTHORIZED

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = add_user(
            **schemas.UserCreateIn(
                username=form.username,
                email=form.email,
                password=hashed_password,
                date_of_birth=form.date_of_birth,
            ).model_dump()
        )
        return user

    return jsonify({'message': 'No user created'}), status.HTTP_307_TEMPORARY_REDIRECT


def login():
    if current_user.is_authenticated:
        return jsonify({'message': 'User is not authenticated'}), status.HTTP_401_UNAUTHORIZED

    form = LoginForm()

    if form.validate_on_submit():
        conn = get_db()
        user_db = repos.User(conn).get_one_by_username(form.username)

        if user_db and bcrypt.check_password_hash(user_db.password, form.password.data):
            login_user(user_db, remember=form.remember.data)

            return jsonify({'message': 'User is authenticated'}), status.HTTP_200_OK
        else:
            return jsonify({'message': 'Login unsuccessful'}), status.HTTP_401_UNAUTHORIZED

    return jsonify({'message': 'No user has logged in'}), status.HTTP_307_TEMPORARY_REDIRECT


def logout():
    logout_user()

    return jsonify({'message': 'User logged out'}), status.HTTP_200_OK

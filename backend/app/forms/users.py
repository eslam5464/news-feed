from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from app import repos
from app.core.db import get_db


class RegistrationForm(FlaskForm):
    username = StringField(
        label='Username',
        validators=[
            DataRequired(),
            Length(min=2, max=20),
        ]
    )
    email = StringField(
        label='Email',
        validators=[DataRequired(), Email()],
    )
    date_of_birth = DateField(
        label='Date of birth',
        validators=[DataRequired()],
    )
    password = PasswordField(
        label='Password',
        validators=[DataRequired()],
    )
    confirm_password = PasswordField(
        label='Confirm Password',
        validators=[DataRequired(), EqualTo('password')],
    )
    submit = SubmitField('Sign Up')

    @staticmethod
    def validate_username(username):
        conn = get_db()
        user = repos.User(conn).get_one_by_username(username.data)

        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    @staticmethod
    def validate_email(email):
        conn = get_db()
        user = repos.User(conn).get_one_by_email(email.data)

        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(
        label='Username',
        validators=[DataRequired(), Length(min=2, max=20)],
    )
    password = PasswordField(
        label='Password',
        validators=[DataRequired()],
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField(
        label='Username',
        validators=[DataRequired(), Length(min=2, max=20)],
    )
    email = StringField(
        label='Email',
        validators=[DataRequired(), Email()],
    )
    submit = SubmitField('Update')

    @staticmethod
    def validate_username(username):
        if username.data != current_user.username:
            conn = get_db()
            user = repos.User(conn).get_one_by_username(username.data)

            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    @staticmethod
    def validate_email(email):
        if email.data != current_user.email:
            conn = get_db()
            user = repos.User(conn).get_one_by_email(email.data)

            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

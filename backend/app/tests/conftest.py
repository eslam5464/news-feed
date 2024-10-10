from datetime import datetime, UTC

import mysql.connector
import pytest

from app import repos, schemas
from app.config import settings
from app.tests.utils import generate_profile, random_password


@pytest.fixture(scope='module')
def db_connection():
    connection = mysql.connector.connect(**settings.database_config)
    yield connection

    connection.rollback()


@pytest.fixture(scope="module", autouse=True)
def new_user(db_connection):
    new_user = generate_profile()
    user_in = schemas.UserCreate(
        username=new_user.username,
        is_active=True,
        creation_timestamp=datetime.now(UTC),
        date_of_birth=new_user.birthdate,
        password=random_password(),
        email=new_user.mail,
    )

    return repos.User(db_connection).create(user_in)

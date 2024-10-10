from datetime import UTC

from win32ctypes.pywin32.pywintypes import datetime

from app import repos
from app.tests.utils import generate_profile, random_password
from backend.app import schemas


def test_create_user(db_connection) -> None:
    new_user = generate_profile()
    date_now = datetime.now(UTC).replace(tzinfo=None)
    user_in = schemas.UserCreate(
        username=new_user.username,
        is_active=True,
        creation_timestamp=date_now,
        date_of_birth=new_user.birthdate,
        password=random_password(),
        email=new_user.mail,
    )
    new_user_id = repos.User(db_connection).create(user_in)

    assert new_user_id

    user = repos.User(db_connection).get_one(new_user_id)

    assert user.model_dump(exclude={"id", "creation_timestamp"}) == user_in.model_dump(exclude={"creation_timestamp"})

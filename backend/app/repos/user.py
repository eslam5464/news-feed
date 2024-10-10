import mysql.connector

from app import schemas

from app.config import settings


class User:
    @staticmethod
    def create(user_in: schemas.UserCreate) -> int:
        conn = mysql.connector.connect(**settings.database_config)
        cursor = conn.cursor()

        query = (
            f"INSERT INTO user (username, password, email, date_of_birth, is_active, creation_timestamp) "
            f"VALUES ('{user_in.username}', '{user_in.password}', "
            f"'{user_in.email}', '{user_in.date_of_birth}', "
            f"{bool(user_in.is_active)}, '{user_in.creation_timestamp}')"
        )
        cursor.execute(query)
        conn.commit()
        user_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return user_id

    @staticmethod
    def get_one(user_id: int) -> schemas.User | None:
        conn = mysql.connector.connect(**settings.database_config)
        cursor = conn.cursor()

        query = f"SELECT * FROM user WHERE id = {user_id}"
        cursor.execute(query)
        user_db = cursor.fetchone()

        cursor.close()
        conn.close()

        if not user_db:
            return None

        return schemas.User(
            id=user_db[0],
            username=user_db[1],
            email=user_db[2],
            password=user_db[3],
            date_of_birth=user_db[4],
            is_active=user_db[5],
            creation_timestamp=user_db[6],
        )

    @staticmethod
    def get_one_by_email(user_email: str) -> schemas.User | None:
        conn = mysql.connector.connect(**settings.database_config)
        cursor = conn.cursor()

        query = f"SELECT * FROM user WHERE email = '{user_email}'"
        cursor.execute(query)
        user_db = cursor.fetchone()

        cursor.close()
        conn.close()

        if not user_db:
            return None

        return schemas.User(
            id=user_db[0],
            username=user_db[1],
            email=user_db[2],
            password=user_db[3],
            date_of_birth=user_db[4],
            is_active=user_db[5],
            creation_timestamp=user_db[6],
        )

    @staticmethod
    def get_one_by_username(user_username: str) -> schemas.User | None:
        conn = mysql.connector.connect(**settings.database_config)
        cursor = conn.cursor()

        query = f"SELECT * FROM user WHERE username = '{user_username}'"
        cursor.execute(query)
        user_db = cursor.fetchone()

        cursor.close()
        conn.close()

        if not user_db:
            return None

        return schemas.User(
            id=user_db[0],
            username=user_db[1],
            email=user_db[2],
            password=user_db[3],
            date_of_birth=user_db[4],
            is_active=user_db[5],
            creation_timestamp=user_db[6],
        )
    @staticmethod
    def get_all() -> list[schemas.User]:
        conn = mysql.connector.connect(**settings.database_config)
        cursor = conn.cursor()

        query = f"SELECT * FROM user"
        cursor.execute(query)
        users_db = cursor.fetchall()

        cursor.close()
        conn.close()

        for user_entry in users_db:
            yield schemas.User(
                id=user_entry[0],
                username=user_entry[1],
                email=user_entry[2],
                password=user_entry[3],
                date_of_birth=user_entry[4],
                is_active=user_entry[5],
                creation_timestamp=user_entry[6],
            )

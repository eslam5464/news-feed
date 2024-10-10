import mysql.connector

from app import schemas

from app.config import settings


class Like:
    @staticmethod
    def create(user_in: schemas.LikeCreate) -> int:
        conn = mysql.connector.connect(**settings.database_config)
        cursor = conn.cursor()

        query = (
            f"INSERT INTO Like (post_id, user_id, creation_timestamp) "
            f"VALUES ('{user_in.post_id}', '{user_in.user_id}', "
            f"'{user_in.creation_timestamp}')"
        )
        cursor.execute(query)
        conn.commit()
        user_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return user_id

    @staticmethod
    def get_one(like_id: int) -> schemas.Like | None:
        conn = mysql.connector.connect(**settings.database_config)
        cursor = conn.cursor()

        query = f"SELECT * FROM like WHERE id = {like_id}"
        cursor.execute(query)
        like_db = cursor.fetchone()

        cursor.close()
        conn.close()

        if not like_db:
            return None

        return schemas.Like(
            id=like_db[0],
            post_id=like_db[1],
            user_id=like_db[2],
            creation_timestamp=like_db[3],
        )

    @staticmethod
    def get_all_by_post_id(post_id: int):
        conn = mysql.connector.connect(**settings.database_config)
        cursor = conn.cursor()

        query = f"SELECT * FROM like WHERE post_id = {post_id}"
        cursor.execute(query)
        likes_db = cursor.fetchall()

        cursor.close()
        conn.close()

        return [
            schemas.Like(
                id=like_entry[0],
                post_id=like_entry[1],
                user_id=like_entry[2],
                creation_timestamp=like_entry[3],
            )
            for like_entry
            in likes_db
        ]

    @staticmethod
    def get_all_by_user_id(user_id: int):
        conn = mysql.connector.connect(**settings.database_config)
        cursor = conn.cursor()

        query = f"SELECT * FROM like WHERE user_id = {user_id}"
        cursor.execute(query)
        likes_db = cursor.fetchall()

        cursor.close()
        conn.close()

        return [
            schemas.Like(
                id=like_entry[0],
                post_id=like_entry[1],
                user_id=like_entry[2],
                creation_timestamp=like_entry[3],
            )
            for like_entry
            in likes_db
        ]
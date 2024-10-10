from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from app import schemas


class Like:
    def __init__(self, conn: PooledMySQLConnection | MySQLConnectionAbstract) -> None:
        self.conn = conn

    def create(self, user_in: schemas.LikeCreate) -> int:
        cursor = self.conn.cursor()

        query = (
            f"INSERT INTO Like (post_id, user_id, creation_timestamp) "
            f"VALUES ('{user_in.post_id}', '{user_in.user_id}', "
            f"'{user_in.creation_timestamp}')"
        )
        cursor.execute(query)
        self.conn.commit()
        user_id = cursor.lastrowid

        cursor.close()

        return user_id

    def get_one(self, like_id: int) -> schemas.Like | None:
        cursor = self.conn.cursor()

        query = f"SELECT * FROM like WHERE id = {like_id}"
        cursor.execute(query)
        like_db = cursor.fetchone()

        cursor.close()

        if not like_db:
            return None

        return schemas.Like(
            id=like_db[0],
            post_id=like_db[1],
            user_id=like_db[2],
            creation_timestamp=like_db[3],
        )

    def get_all_by_post_id(self, post_id: int):
        cursor = self.conn.cursor()

        query = f"SELECT * FROM like WHERE post_id = {post_id}"
        cursor.execute(query)
        likes_db = cursor.fetchall()

        cursor.close()

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

    def get_all_by_user_id(self, user_id: int):
        cursor = self.conn.cursor()

        query = f"SELECT * FROM like WHERE user_id = {user_id}"
        cursor.execute(query)
        likes_db = cursor.fetchall()

        cursor.close()

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

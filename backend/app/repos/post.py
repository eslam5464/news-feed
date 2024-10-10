from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from app import schemas


class Post:
    def __init__(self, conn: PooledMySQLConnection | MySQLConnectionAbstract) -> None:
        self.conn = conn

    def create(self, post_in: schemas.PostCreate) -> int:
        cursor = self.conn.cursor()

        query = (
            f"INSERT INTO post (user_id, content, creation_timestamp, modification_timestamp) "
            f"VALUES ('{post_in.user_id}', '{post_in.content}', "
            f"'{post_in.creation_timestamp}', '{post_in.modification_timestamp}')"
        )
        cursor.execute(query)
        self.conn.commit()
        user_id = cursor.lastrowid

        cursor.close()

        return user_id

    def get_one(self, post_id: int) -> schemas.Post | None:
        cursor = self.conn.cursor()

        query = f"SELECT * FROM post WHERE id = {post_id}"
        cursor.execute(query)
        post_db = cursor.fetchone()

        cursor.close()

        if not post_db:
            return None

        return schemas.Post(
            id=post_db[0],
            user_id=post_db[1],
            content=post_db[2],
            creation_timestamp=post_db[3],
            modification_timestamp=post_db[4],
        )

    def get_all_by_user_id(self, user_id: int) -> list[schemas.Post]:
        cursor = self.conn.cursor()

        query = f"SELECT * FROM post WHERE user_id = {user_id}"
        cursor.execute(query)
        posts_db = cursor.fetchall()

        cursor.close()

        return [
            schemas.Post(
                id=post_entry[0],
                user_id=post_entry[1],
                content=post_entry[2],
                creation_timestamp=post_entry[3],
                modification_timestamp=post_entry[4],
            )
            for post_entry
            in posts_db
        ]

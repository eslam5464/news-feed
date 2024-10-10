from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from app import schemas


class Comment:
    def __init__(self, conn: PooledMySQLConnection | MySQLConnectionAbstract) -> None:
        self.conn = conn

    def create(self, user_in: schemas.CommentCreate) -> int:
        cursor = self.conn.cursor()

        query = (
            f"INSERT INTO comment (post_id, user_id, content, creation_timestamp) "
            f"VALUES ('{user_in.post_id}', '{user_in.user_id}', "
            f"'{user_in.content}', '{user_in.creation_timestamp}')"
        )
        cursor.execute(query)
        self.conn.commit()
        user_id = cursor.lastrowid

        cursor.close()

        return user_id

    def get_one(self,comment_id: int):
        cursor = self.conn.cursor()

        query = f"SELECT * FROM comment WHERE comment_id = {comment_id}"
        cursor.execute(query)
        comment_db = cursor.fetchone()

        cursor.close()

        return schemas.Comment(
            id=comment_db[0],
            user_id=comment_db[1],
            post_id=comment_db[2],
            content=comment_db[3],
            creation_timestamp=comment_db[4],
        )

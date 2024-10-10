import mysql.connector

from app import schemas

from app.config import settings


class Comment:
    @staticmethod
    def create(user_in: schemas.CommentCreate) -> int:
        conn = mysql.connector.connect(**settings.database_config)
        cursor = conn.cursor()

        query = (
            f"INSERT INTO comment (post_id, user_id, content, creation_timestamp) "
            f"VALUES ('{user_in.post_id}', '{user_in.user_id}', "
            f"'{user_in.content}', '{user_in.creation_timestamp}')"
        )
        cursor.execute(query)
        conn.commit()
        user_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return user_id

    @staticmethod
    def get_one(comment_id: int):
        conn = mysql.connector.connect(**settings.database_config)
        cursor = conn.cursor()

        query = f"SELECT * FROM comment WHERE comment_id = {comment_id}"
        cursor.execute(query)
        comment_db = cursor.fetchone()

        cursor.close()
        conn.close()

        return schemas.Comment(
            id=comment_db[0],
            user_id=comment_db[1],
            post_id=comment_db[2],
            content=comment_db[3],
            creation_timestamp=comment_db[4],
        )

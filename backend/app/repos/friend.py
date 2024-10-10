import mysql.connector

from app import schemas

from app.config import settings


class Friend:
    @staticmethod
    def create(user_in: schemas.FriendCreate) -> int:
        conn = mysql.connector.connect(**settings.database_config)
        cursor = conn.cursor()

        query = (
            f"INSERT INTO Friend (user_id, friend_id, creation_timestamp) "
            f"VALUES ('{user_in.user_id}', '{user_in.friend_id}', "
            f"'{user_in.creation_timestamp}')"
        )
        cursor.execute(query)
        conn.commit()
        user_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return user_id


    @staticmethod
    def get_all_by_user_id(user_id:int) -> list[schemas.Friend]:
        conn = mysql.connector.connect(**settings.database_config)
        cursor = conn.cursor()

        query = f"SELECT * FROM user WHERE user_id = {user_id}"
        cursor.execute(query)
        friends_db = cursor.fetchall()

        cursor.close()
        conn.close()

        return [
            schemas.Friend(
                id=friend_entry[0],
                user_id=friend_entry[1],
                friend_id=friend_entry[2],
                creation_timestamp=friend_entry[3],
            )
            for friend_entry
            in friends_db
        ]
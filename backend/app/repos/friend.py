from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from app import schemas


class Friend:
    def __init__(self, conn: PooledMySQLConnection | MySQLConnectionAbstract) -> None:
        self.conn = conn

    def create(self, user_in: schemas.FriendCreate) -> int:
        cursor = self.conn.cursor()

        query = (
            f"INSERT INTO Friend (user_id, friend_id, creation_timestamp) "
            f"VALUES ('{user_in.user_id}', '{user_in.friend_id}', "
            f"'{user_in.creation_timestamp}')"
        )
        cursor.execute(query)
        self.conn.commit()
        user_id = cursor.lastrowid

        cursor.close()

        return user_id

    def get_all_by_user_id(self,user_id: int) -> list[schemas.Friend]:
        cursor = self.conn.cursor()

        query = f"SELECT * FROM user WHERE user_id = {user_id}"
        cursor.execute(query)
        friends_db = cursor.fetchall()

        cursor.close()

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

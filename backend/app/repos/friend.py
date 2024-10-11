from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from app import schemas


class Friend:
    def __init__(self, conn: PooledMySQLConnection | MySQLConnectionAbstract) -> None:
        self.conn = conn

    def create(self, user_in: schemas.FriendCreate) -> int:
        cursor = self.conn.cursor()

        query = (
            f"INSERT INTO friend (user_id, friend_id, creation_timestamp) "
            f"VALUES ('{user_in.user_id}', '{user_in.friend_id}', "
            f"'{user_in.creation_timestamp}')"
        )
        cursor.execute(query)
        self.conn.commit()
        user_id = cursor.lastrowid

        cursor.close()

        return user_id

    def get(self, user_id: int, friend_id: int):
        cursor = self.conn.cursor()

        query = f"SELECT * FROM friend WHERE user_id = {user_id} and friend_id = {friend_id}"
        cursor.execute(query)
        friend_db = cursor.fetchone()

        cursor.close()

        if not friend_db:
            return None

        return schemas.Friend(
            id=friend_db[0],
            user_id=friend_db[1],
            friend_id=friend_db[2],
            creation_timestamp=friend_db[3],
        )

    def get_all_by_user_id(self, user_id: int) -> list[schemas.Friend]:
        cursor = self.conn.cursor()

        query = f"SELECT * FROM friend WHERE user_id = {user_id}"
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

    def delete(self, user_id: int, friend_id: int):
        cursor = self.conn.cursor()

        query = f"DELETE FROM friend WHERE user_id = {user_id} AND friend_id = {friend_id}"
        cursor.execute(query)

        self.conn.commit()
        cursor.close()

        return None

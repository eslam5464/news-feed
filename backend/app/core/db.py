import mysql.connector
from flask import g
from flask_bcrypt import Bcrypt

from app.core.config import settings

bcrypt = Bcrypt()


def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(**settings.database_config)

    return g.db

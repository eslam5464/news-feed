import mysql.connector
from flask import g

from app.config import settings


def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(**settings.database_config)

    return g.db

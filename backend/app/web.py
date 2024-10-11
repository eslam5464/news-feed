from flask import Flask, g

from app.config import settings
from app.db import get_db

from app.routes import user, auth, post


def create_app(config_class=settings):
    app = Flask(settings.app_name)
    app.config.from_object(config_class)

    app.register_blueprint(user)
    app.register_blueprint(auth)
    app.register_blueprint(post)

    @app.before_request
    def setup_db():
        g.db = get_db()

    @app.teardown_appcontext
    def close_db(exception):
        db = g.pop('db', None)

        if db is not None:
            db.close()

    return app

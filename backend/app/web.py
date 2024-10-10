from flask import Flask

from app.config import settings

from app.routes import user


def create_app(config_class=settings):
    app = Flask(settings.app_name)
    app.config.from_object(config_class)

    app.register_blueprint(user)

    return app

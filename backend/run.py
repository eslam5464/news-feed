from app.config import settings
from app.web import create_app

app = create_app()

if __name__ == '__main__':
    app.run(
        debug=settings.debug,
        host=settings.host,
        port=settings.port,
    )
from flask import Flask

from slack_doc.cache import Cache

# redis_client = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=os.environ.get("REDIS_PORT", 6379), db=0)
app_cache = Cache()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    # app.config.from_object('config.Config')

    with app.app_context():
        from . import routes

        return app

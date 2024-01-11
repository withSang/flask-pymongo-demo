from flask import Flask

from config import Config
from database import mongo
from app.api import echo_blueprint, image_blueprint

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Database initialization
    mongo.init_app(app)

    # Register blueprints
    app.register_blueprint(echo_blueprint, url_prefix="/echo")
    app.register_blueprint(image_blueprint, url_prefix="/image")

    return app

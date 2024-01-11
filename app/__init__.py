from flask import Flask
from config import Config

from app.api import echo_blueprint

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(echo_blueprint)

    return app

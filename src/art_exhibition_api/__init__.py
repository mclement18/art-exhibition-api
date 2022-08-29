from flask import Flask

from . import db
from .config import Config

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config())

    db.init_app(app)
    
    return app
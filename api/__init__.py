from flask import Flask
from api.extenstions import db, ma
from config import config_by_name
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_by_name[os.getenv("FLASK_ENV")])
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()
    return app



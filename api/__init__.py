from flask import Flask
from flask_restx import Api
from api.extenstions import db, ma
from api.config import config_by_name
from api.customers import register_routes
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_by_name[os.getenv("FLASK_ENV")])
    db.init_app(app)
    ma.init_app(app)

    api = Api(app, title="Customers Platform APIs", version="0.1")

    register_routes(api)

    with app.app_context():
        db.create_all()
    return app



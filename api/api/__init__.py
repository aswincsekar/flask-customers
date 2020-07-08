from flask import Flask, jsonify
from flask_restx import Api
from api.extenstions import db, ma, jwt
from api.config import config_by_name
from customers import register_routes as customer_routes
from authentication import register_routes as authentication_routes
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_by_name[os.getenv("FLASK_ENV")])
    app.config['PROPAGATE_EXCEPTIONS'] = True
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    api = Api(app, title="Customers Platform APIs", version="0.1")
    jwt._set_error_handler_callbacks(api)

    # Using the expired_token_loader decorator, we will now call
    # this function whenever an expired but otherwise valid access
    # token attempts to access an endpoint
    @jwt.invalid_token_loader
    def my_invalid_token_callback(msg):
        return {
            'msg': 'The {} token is invalid'.format('JWT')
        }, 401

    @jwt.expired_token_loader
    def my_expired_token_callback(msg):
        return {
            'msg': 'The {} token is expired'.format('JWT')
        }, 401

    @jwt.token_in_blacklist_loader
    def my_blacklist_token_callback(msg):
        return {
            'msg': 'The {} token is blacklisted'.format('JWT')
        }, 401

    @jwt.unauthorized_loader
    def unauthorized_token_callback(msg):
        return {
                   'msg': 'Unauthorized Access'
        }, 401


    customer_routes(api)
    authentication_routes(api)

    with app.app_context():
        db.create_all()
    return app



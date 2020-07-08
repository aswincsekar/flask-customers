from flask import jsonify
from flask import request
from flask_restx import Resource, Namespace
from flask_accepts import accepts, responds
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, jwt_refresh_token_required, get_raw_jwt, create_refresh_token

)
from authentication.schemes import LoginScheme

blacklist = set()

api = Namespace(
    "Authentication",
    description="Help's you to manage JWT Tokens"
)


@api.route('/login')
class LoginResource(Resource):
    @accepts(schema=LoginScheme, api=api)
    def post(self):
        data = request.parsed_obj

        username = data.get('username', None)
        password = data.get('password', None)
        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        if username != 'test' or password != 'test':
            return jsonify({"msg": "Bad username or password"}), 401

        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)

        return {"access_token": access_token, "refresh_token": refresh_token}, 200


@api.route('/refresh')
class RefreshResource(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        ret = {
            'access_token': create_access_token(identity=current_user),
            'refresh_token': create_refresh_token(identity=current_user)
        }
        return ret, 200


@api.route('/logout')
class LogoutResource(Resource):
    @jwt_required
    def delete(self):
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
        return {"msg": "Successfully logged out"}, 200


@api.route('/protected')
class ProtectedResource(Resource):
    @jwt_required
    def get(self):
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        return {"logged_in_as": current_user}, 200

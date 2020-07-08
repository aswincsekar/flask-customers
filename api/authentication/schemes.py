from api import ma
from marshmallow import fields, EXCLUDE


class LoginScheme(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

    class Meta:
        unknown = EXCLUDE
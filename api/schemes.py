from api import ma
from marshmallow import fields, EXCLUDE


class CustomerScheme(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    dob = fields.Date(required=False)
    updated_at = fields.DateTime(required=True)

    class Meta:
        unknown = EXCLUDE


customer_scheme = CustomerScheme()
customers_scheme = CustomerScheme(many=True)
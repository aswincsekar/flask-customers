from flask import request
from flask_restx import Resource, Namespace
from flask_restx.errors import abort
from datetime import datetime
from api import db
from customers.models import Customer
from customers.schemes import CustomerScheme
from flask_accepts import accepts, responds
from sqlalchemy import desc
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity
)


api = Namespace(
    "Customers",
    description="Help's you to manage customers"
)


@api.route('/customers/')
class CustomerList(Resource):
    @jwt_required
    @responds(schema=CustomerScheme(many=True), api=api, status_code=200)
    def get(self):
        customers = Customer.query.all()
        return customers

    @jwt_required
    @accepts(schema=CustomerScheme(exclude=("id",)), api=api)
    @responds(schema=CustomerScheme, api=api, status_code=201)
    def post(self):
        data = request.parsed_obj
        customer = Customer(name=data['name'], dob=data.get('dob', None),
                            updated_at=datetime.now())
        db.session.add(customer)
        db.session.commit()
        return customer


@api.route('/nyoungest/<int:n>')
class NYoungCustomerList(Resource):
    @jwt_required
    @responds(schema=CustomerScheme(many=True), api=api, status_code=200)
    def get(self, n):
        customers = Customer.query.order_by(desc(Customer.dob)).limit(n).all()
        return customers


@api.route('/customers/<string:customer_id>')
class CustomerDetail(Resource):
    @jwt_required
    @responds(schema=CustomerScheme, api=api, status_code=200)
    def get(self, customer_id):
        customer = Customer.query.get(customer_id)
        if customer:
            return customer
        else:
            abort(404, "Customer ID Not Found")

    @jwt_required
    @accepts(schema=CustomerScheme, api=api, partial=True)
    @responds(schema=CustomerScheme, api=api, status_code=200)
    def put(self, customer_id):
        changes = request.parsed_obj
        changes['updated_at'] = datetime.now()
        resp = Customer.query.filter_by(id=customer_id).update(changes)
        db.session.commit()
        return Customer.query.get(customer_id)

    @api.response(204, "Customer deleted")
    def delete(self, customer_id):
        customer = Customer.query.get(customer_id)
        db.session.delete(customer)
        db.session.commit()
        return '', 204




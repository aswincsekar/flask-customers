from flask import request
from flask_restx import Resource, fields, Api
from flask_restx.errors import abort
from datetime import datetime
from api import db, create_app
from api.models import Customer
from api.schemes import CustomerScheme
from flask_accepts import accepts, responds

app = create_app()

api = Api(app)


@api.route('/customer/')
class CustomerList(Resource):
    @responds(schema=CustomerScheme(many=True), api=api, status_code=200)
    def get(self):
        customers = Customer.query.all()
        return customers

    @accepts(schema=CustomerScheme(exclude=("id",)), api=api)
    @responds(schema=CustomerScheme, api=api, status_code=201)
    def post(self):
        data = request.parsed_obj
        customer = Customer(name=data['name'], dob=data.get('dob', None),
                            updated_at=datetime.now())
        db.session.add(customer)
        db.session.commit()
        return customer


@api.route('/customer/<string:customer_id>')
class CustomerDetail(Resource):
    @responds(schema=CustomerScheme, api=api, status_code=200)
    def get(self, customer_id):
        customer = Customer.query.get(customer_id)
        if customer:
            return customer
        else:
            abort(404, "Customer ID Not Found")

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


if __name__ == '__main__':
    app.run()

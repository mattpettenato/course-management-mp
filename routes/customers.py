from flask import Blueprint, jsonify
from models.Customer import Customer
from app import db

customers_bp = Blueprint('customers', __name__, url_prefix='/api/customers')

# route to get the list of customers
@customers_bp.route('/api/customers', methods=['GET'])
def get_customers():
    # Get all the customers from the database
    customers = Customer.query.all()
    results = []

    # Convert the Customer objects to a list of dictionaries
    for customer in customers:
        customer_dict = {
            'id': customer.id,
            'name': customer.name,
            'email': customer.email,
            'password': customer.password
        }
        results.append(customer_dict)

    return jsonify(results)

from flask import Blueprint, jsonify
from ..models.Employee import Employee
from ..database import db

employees_bp = Blueprint('employee', __name__, url_prefix='/api/employees')

# Route to get the list of employees


@employees_bp.route('/api/employees', methods=['GET'])
def get_employees():
    # Get all the employees from the database
    employees = Employee.query.all()
    results = []

    # Convert the Employee objects to a list of dictionaries
    for employee in employees:
        employee_dict = {
            'id': employee.id,
            'name': employee.name,
            'email': employee.email,
            'password': employee.password
        }
        results.append(employee_dict)

    return jsonify(results)

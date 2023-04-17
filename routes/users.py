from flask import Blueprint, jsonify
from app import db
from models import User

users_bp = Blueprint('users', __name__, url_prefix='/api/users')


# Route to get the list of users
@users_bp.route('', methods=['GET'])
def get_users():
    # Get all the users from the database
    users = User.query.all()
    results = []

    # Convert the User objects to a list of dictionaries
    for user in users:
        user_dict = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'password': user.password
        }
        results.append(user_dict)

    return jsonify(results)

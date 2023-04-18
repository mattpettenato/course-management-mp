import jwt
from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash
from .. import db
from models.User import User
from flask import current_app as app

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

# Route for user login

@users_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    # Check if email and password are provided
    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    # Check if the provided email matches with any user in the database
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Check if the provided password matches with the user's password in the database
    if not check_password_hash(user.password, password):
        return jsonify({'error': 'Incorrect password'}), 401

    # Create a JWT token
    token_payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    token = jwt.encode(
        token_payload, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token}), 200

# Route to create a new user

@users_bp.route('/register', methods=['POST'])
def create_user():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')

    # Check if name, email and password are provided
    if not name or not email or not password:
        return jsonify({'error': 'Name, email and password are required'}), 400

    # Check if the provided email matches with any user in the database
    user = User.query.filter_by(email=email).first()

    if user:
        return jsonify({'error': 'Email already in use'}), 409

    # Create a new user
    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

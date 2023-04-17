from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/golfcourse'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)


# Import the routes
from routes.users import users_bp
from routes.tee_times import tee_times_bp
from routes.schedules import schedules_bp
from routes.employees import employees_bp
from routes.customers import customers_bp
from routes.bookings import bookings_bp

# Import the models
from models.TeeTime import TeeTime
from models.User import User
from models.Booking import Booking
from models.Employee import Employee
from models.Schedule import Schedule
from models.Customer import Customer

# Register the routes with the app
app.register_blueprint(users_bp)
app.register_blueprint(tee_times_bp)
app.register_blueprint(schedules_bp)
app.register_blueprint(employees_bp)
app.register_blueprint(customers_bp)
app.register_blueprint(bookings_bp)

# Run the app
if __name__ == '__main__':
    app.run()


# Default route


@app.route('/')
def index():
    return 'Hello, World!'


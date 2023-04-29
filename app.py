from . import models
from .database import db
from .models.TeeTime import TeeTime
from .models.Booking import Booking
from .models.Employee import Employee
from .models.Schedule import Schedule
from .models.Customer import Customer
from .models.User import User
from .routes.tee_times import tee_times_bp
from .routes.schedules import schedules_bp
from .routes.employees import employees_bp
from .routes.customers import customers_bp
from .routes.bookings import bookings_bp
from .routes.users import users_bp
from flask_migrate import Migrate
from flask import Flask

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://thomasp:Pett29@localhost/golfcourse'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Initialize migrations
migrate = Migrate(app, db)

# Import the models

# Register the blueprints with the app
app.register_blueprint(users_bp)
app.register_blueprint(bookings_bp)
app.register_blueprint(customers_bp)
app.register_blueprint(employees_bp)
app.register_blueprint(schedules_bp)
app.register_blueprint(tee_times_bp)

# app.register_blueprint(users_bp)
# app.register_blueprint(bookings_bp)
# app.register_blueprint(customers_bp)
# app.register_blueprint(employees_bp)
# app.register_blueprint(schedules_bp)
# app.register_blueprint(tee_times_bp)

# Default route


@app.route('/')
def index():
    return 'Hello, World!'


# Run the app
if __name__ == '__main__':
    app.run()

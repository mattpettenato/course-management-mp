from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/golfcourse'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the TeeTime model


class TeeTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<TeeTime %r>' % self.time

# Route to get the list of tee times


@app.route('/api/tee_times', methods=['GET'])
def get_tee_times():
    # Get all the tee times from the database
    tee_times = TeeTime.query.all()
    results = []

    # Convert the TeeTime objects to a list of dictionaries
    for tee_time in tee_times:
        tee_time_dict = {
            'id': tee_time.id,
            'time': tee_time.time
        }
        results.append(tee_time_dict)

    return jsonify(results)

# Route to book a new tee time

@app.route('/api/book_tee_time', methods=['POST'])
def book_tee_time():
    data = request.json
    # TODO: Implement code to book a new tee time in database
    success = True
    return jsonify(success=success)

# Default route


@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
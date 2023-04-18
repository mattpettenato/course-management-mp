from flask import Blueprint, jsonify
from ..models.Booking import Booking
from ..database import db

bookings_bp = Blueprint('bookings', __name__)

# Route to get the list of bookings
@bookings_bp.route('/api/bookings', methods=['GET'])
def get_bookings():
    # Get all the bookings from the database
    bookings = Booking.query.all()
    results = []

    # Convert the Booking objects to a list of dictionaries
    for booking in bookings:
        booking_dict = {
            'id': booking.id,
            'user_id': booking.user_id,
            'tee_time_id': booking.tee_time_id
        }
        results.append(booking_dict)

    return jsonify(results)

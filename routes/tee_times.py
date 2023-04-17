from flask import Blueprint, jsonify
from models.TeeTime import TeeTime

tee_times_bp = Blueprint('tee_times', __name__)

# Route to get the list of tee times


@tee_times_bp.route('/api/tee_times', methods=['GET'])
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


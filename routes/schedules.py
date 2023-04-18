from flask import Blueprint, jsonify
from ..models.Schedule import Schedule
# from app import db
from ..database import db


schedules_bp = Blueprint('schedules', __name__)

# route to get the list of schedules
@schedules_bp.route('/api/schedules', methods=['GET'])
def get_schedules():
    # Get all the schedules from the database
    schedules = Schedule.query.all()
    results = []

    # Convert the Schedule objects to a list of dictionaries
    for schedule in schedules:
        schedule_dict = {
            'id': schedule.id,
            'employee_id': schedule.employee_id,
            'tee_time_id': schedule.tee_time_id
        }
        results.append(schedule_dict)

    return jsonify(results)

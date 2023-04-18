# from ..app import db
from ..database import db



# Define the schedule model


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey(
        'employee.id'), nullable=False)
    tee_time_id = db.Column(db.Integer, db.ForeignKey(
        'tee_time.id'), nullable=False)

    def __repr__(self):
        return '<Schedule %r>' % self.id

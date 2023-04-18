# from ..app import db
from ..database import db

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tee_time_id = db.Column(db.Integer, db.ForeignKey(
        'tee_times.id'), nullable=False)
    user = db.relationship('User', backref='bookings', lazy=True)

    def __repr__(self):
        return '<Booking %r>' % self.id
    
    

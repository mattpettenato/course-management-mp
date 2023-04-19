from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .TeeTime import TeeTime

print("Importing Booking class...")
# from .Booking import Booking

db = SQLAlchemy()


class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tee_time_id = db.Column(db.Integer, db.ForeignKey(
        'tee_times.id'), nullable=False)

    def __repr__(self):
        return '<Booking %r>' % self.id

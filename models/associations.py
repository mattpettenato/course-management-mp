from flask_sqlalchemy import SQLAlchemy
from models.Booking import Booking
from models.TeeTime import TeeTime
from models.User import User
import bcrypt

db = SQLAlchemy()
# Define the association table for the many-to-many relationship
user_tee_times = db.Table('user_tee_times',
                          db.Column('user_id', db.Integer, db.ForeignKey(
                              'users.id'), primary_key=True),
                          db.Column('tee_time_id', db.Integer, db.ForeignKey(
                              'tee_times.id'), primary_key=True)
                          )

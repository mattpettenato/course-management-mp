from .Booking import Booking
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import bcrypt

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    bookings = db.relationship('Booking', backref='user', lazy=True)

    # Define the relationship with the TeeTime class
    teetimes = db.relationship('TeeTime', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.checkpw(
            password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def __repr__(self):
        return '<User %r>' % self.name


# Add the query property to the User model
User.query = db.session.query_property()

# Add the relationships after the dependent classes have been defined
Booking.user_id = db.ForeignKey(User.id)

# Import the Booking class after the User class has been defined

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models.TeeTime import TeeTime
from models.Booking import Booking
from app import db
# from ..database import db
import bcrypt

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    bookings = db.relationship('Booking', backref='user', lazy=True)
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


User.bookings = db.relationship('Booking', backref='user', lazy=True)
# Add query property to the User model
User.query = db.session.query_property()

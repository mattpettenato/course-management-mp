from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from App import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    tee_times = db.relationship(
        'TeeTime', secondary='user_tee_times', backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User %r>' % self.name


# Define the association table for the many-to-many relationship
user_tee_times = db.Table('user_tee_times',
                          db.Column('user_id', db.Integer, db.ForeignKey(
                              'user.id'), primary_key=True),
                          db.Column('tee_time_id', db.Integer, db.ForeignKey(
                              'tee_time.id'), primary_key=True)
                          )

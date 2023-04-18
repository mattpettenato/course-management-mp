# from ..app import db
from ..database import db


# Define the Customer model


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    bookings = db.relationship('Booking', backref='customer', lazy=True)

    def __repr__(self):
        return '<Customer %r>' % self.name

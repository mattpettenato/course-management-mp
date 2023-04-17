from App import db


# Define the Employee model


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    bookings = db.relationship('Booking', backref='employee', lazy=True)

    def __repr__(self):
        return '<Employee %r>' % self.name

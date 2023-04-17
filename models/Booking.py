from App import db


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tee_time_id = db.Column(db.Integer, db.ForeignKey(
        'tee_time.id'), nullable=False)

    def __repr__(self):
        return '<Booking %r>' % self.id

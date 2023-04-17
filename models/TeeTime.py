from App import db

class TeeTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<TeeTime %r>' % self.time

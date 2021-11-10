from app import db

class Cities(db.Model):
    name = db.Column(db.String(64), unique=True, index=True)
    rank = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Cities ()> '.format(self.name)

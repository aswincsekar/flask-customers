from api import db
from datetime import datetime

# Alias common DB names
Column = db.Column
Model = db.Model


class Customer(Model):
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(64), unique=True)
    dob = Column(db.Date, nullable=True)
    updated_at = Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Customer %r>' % self.name

    def __str__(self):
        return self.name

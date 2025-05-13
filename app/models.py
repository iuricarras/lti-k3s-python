from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    ip = db.Column(db.String(100), unique=True)
    token = db.Column(db.String(1000))
    #username = db.Column(db.String(1000))

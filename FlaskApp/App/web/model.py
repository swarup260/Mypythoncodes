from App import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(160), unique=False, nullable=False)
    profile_img = db.Column(db.String(160), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(80), unique=False, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

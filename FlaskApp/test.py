from flask import Flask
import os
from datetime import datetime
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# from flask_mongoalchemy import MongoAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['MONGOALCHEMY_DATABASE'] = 'flaskapp'
# app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://swarup260:14919755#WAS@ds133961.mlab.com:33961/flaskapp'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(BASE_DIR, 'app.db')
#mongo = MongoAlchemy(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(160), unique=False, nullable=False)
    profile_img = db.Column(db.String(160), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(80), unique=False, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)



# @app.route('/')
# def home():
#     return "hello WOrld"


# app.run()

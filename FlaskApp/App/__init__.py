from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__,template_folder='../templates')
app.config.from_object('config')

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


from App.api.route import mod
from App.web.route import mod


app.register_blueprint(api.route.mod,url_prefix='/api') 
app.register_blueprint(web.route.mod)

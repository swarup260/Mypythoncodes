from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,EqualTo,length,Email,ValidationError
from App.web.model import User

class Signin(FlaskForm):
    name = StringField('name', validators=[DataRequired(),length(min=5,max=10)])
    email = StringField('email', validators=[DataRequired(),Email()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password' ,validators=[DataRequired(),length(min=10,max=20)])
    confirm_password = PasswordField('confirm_password' ,validators=[DataRequired(),EqualTo('password') ])
    submit = SubmitField('SignIn')

    #custom validate 
    """ 
        validate_field(self,field):
                custom logic.
    """
    def validate_username(self, username):
        exist_user = User.query.filter(User.username == self.username.data).first()
        if exist_user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        exist_user = User.query.filter(User.email == self.email.data).first()
        if exist_user:
            raise ValidationError('email address already exists.Please choose a different one')

class Login(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password' ,validators=[DataRequired(),length(min=10,max=20)])
    submit = SubmitField('Login')


class ImageUpload(FlaskForm):
    profile = FileField('file upload',validators=[FileAllowed(['jpg','png','jpeg','gif'])])
    submit = SubmitField('upload')


class PostUpload(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    body = TextAreaField('body' ,validators=[DataRequired()] )
    submit = SubmitField('upload')



class Update(FlaskForm):
    name = StringField('name', validators=[DataRequired(),length(min=5,max=10)])
    email = StringField('email', validators=[DataRequired(),Email()])
    username = StringField('username', validators=[DataRequired()])
    newpassword = PasswordField('password' ,validators=[DataRequired(),length(min=10,max=20)])
    confirm_password = PasswordField('confirm_password' ,validators=[DataRequired(),EqualTo('newpassword') ])
    submit = SubmitField('SignIn')

    def validate_email(self, email):
        exist_user = User.query.filter(User.email == self.email.data).first()
        if exist_user:
            raise ValidationError('email address already exists.Please choose a different one')
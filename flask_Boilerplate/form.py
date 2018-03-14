from flask_wtf import Form
from wtforms import TextField, PasswordField, RadioField, validators

class Signupform(Form):
    #name field
    name = TextField('name', [validators.Length(
        min=5, max=15)], validators.Required("Please enter your name."))
    #username field
    username = TextField('username', [validators.Length(
        min=5, max=10), validators.Required("Please enter your username.")])
    #email
    email = TextField('email', [validators.Length(
        min=5, max=15), validators.Required("Please enter your email address."),
        validators.Email("Please enter a valid email")])
    #gender
    gender = RadioField('gender',choices = [('M'),('F')])
    #password
    password = PasswordField('password',[validators.Length(min=5,max=10),
        validators.DataRequired(),
        validators.EqualTo('repassword',message ="MisMatch") ])
    #repassword
    repassword = PasswordField('Repeat Password')


class Signinform(Form):
    email = TextField('email',[validators.Email("enter a valid Email"),
            validators.Required("Please enter the email")])
    password = PasswordField('password',[validators.Required("Please enter the password"),
        validators.Length(min=5,max=10)])

from flask import Flask,render_template,flash,request,session,logging,redirect,url_for
from form import Signupform,Signinform
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/signin',methods=['GET','POST'])
def signin():
    return render_template('signin.html')
    


@app.route('/signup',methods=['GET','POST'])
def signup():
    return render_template('siginup.html')

''' Run the flask application  
Debug mode
'''
if __name__ == '__main__':
    app.run(debug= True)

from flask import Flask,render_template,url_for,flash,redirect,session,logging,request,jsonify
from form import Signupform,Signinform
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
from ScrapingData import MyAnimeList

app = Flask(__name__)
data = MyAnimeList(2018,'summer')


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
    form = Signupform(request.form)
    if(request.method == 'POST' and form.validate()):
        return render_template('siginup.html')
    # return render_template('siginup.html')


@app.route('/json')
def json():
    repsData =  data.scrapingData()
    return jsonify(repsData)


@app.errorhandler(404)
def error(e):
    return render_template('404.html')
''' Run the flask application  
Debug mode
'''
if __name__ == '__main__':
    app.run(debug= True)

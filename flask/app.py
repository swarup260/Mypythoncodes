from flask import Flask,render_template,flash,redirect,url_for,session,logging
app = Flask(__name__)
@app.route('/') #route which simply return a value
def home():
    return render_template('home.html')
''' 
route which return a templates 
templates
|--home.html
'''
@app.route('/about')
def about():
    return render_template('about.html',optional_params= [1,2,3])

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/register')
def register():
    return render_template('register.html')
''' route which return a templates 
with a GET params in url
string:var_name i.e the params is a string
string ->accepts any text without a slash (the default)
int->accepts integers
float ->like int but for floating point values
path ->like the default but also accepts slashes
any ->matches one of the items provided
uuid->accepts UUID strings
'''
@app.route('/post/<string:var_name>')
def post(var_name):
    return render_template('post.html',optional_params=var_name)

'''
Run the flask application  
Debug mode
'''
if __name__ == '__main__':
    app.run(debug= True)

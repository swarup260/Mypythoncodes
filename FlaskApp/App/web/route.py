from flask import Blueprint, render_template, url_for, redirect, jsonify,session,request,flash
from App.web.form import Signin, Login, ImageUpload, PostUpload,Update
from App.web.model import User, Post
from App import db,bcrypt,app
from datetime import datetime
#IMAGE UPLOAD
import os
import secrets
from PIL import Image



mod = Blueprint('web',__name__,template_folder='./templates',static_folder='./static')


@mod.route('/home')
@mod.route('/')
def home():
    if session:
        flash(f"{session['user_username']} is Logged in", 'teal lighten-2')
        return render_template('home.html')
    return render_template('home.html')


@mod.route('/about')
def about():
    return render_template('about.html')


@mod.route('/register',methods= ['GET','POST'] )
def register():
    form = Signin()

    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data,10).decode('utf-8')
        user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                    password=hash_password, profile_img='default.jpg')
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'teal lighten-2')
        # user.insert({'name': form.username.data, 'password': form.password.data})
        return redirect(url_for('web.login'))
    return render_template('register.html',form = form)


@mod.route('/login', methods= ['GET','POST'] )
def login():
    form = Login()
    if form.validate_on_submit():
        result = User.query.filter_by(username = form.username.data).first()
        if result:
            session['user_username'] = form.username.data
            if bcrypt.check_password_hash(result.password, form.password.data):
                return redirect(url_for('web.home'))
            else:
                flash('invalid password', 'red lighten-2')
        else:
            flash('Invalid username', 'red lighten-2')
    return render_template('login.html',form = form)


@mod.route('/logout')
def logout():
    session.clear()
    flash('SuccessFully Logout!', 'teal lighten-2')
    return render_template('home.html')



def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'static\\profile_pics', picture_fn)

    output_size = (150, 150)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@mod.route('/myaccount', methods=['POST', 'GET'])
def myaccount():
    form = ImageUpload()
    user = User.query.filter_by(username = session['user_username']).first()
    if form.validate_on_submit():
        picture_file = save_picture(form.profile.data)
        user.profile_img = picture_file
        db.session.add(user)
        db.session.commit()
        flash('Image Upload Scuccessfully !!!')
        return redirect(url_for('web.myaccount'))
    return render_template('profile.html', form=form, user=user)



@mod.route('/post')
def post():
    id = request.args.get('id', 0)
    if id:
        return render_template('singlepost.html', id=id)
    return render_template('post.html')


@mod.route('/userpost' , methods = ['POST','GET'])
def userpost():
    if session:
        user = User.query.filter_by(username = session['user_username']).first()
    form = PostUpload()
    if form.validate_on_submit():
        setpost = Post(title=form.title.data, body=form.body.data,
                       image='defaultPost.jpg', userId=user.id)
        db.session.add(setpost)
        db.session.commit()
        flash('SuccessFully post uploaded', 'teal lighten-2')
        return redirect(url_for('web.myaccount'))
    return render_template('uploadpost.html', form=form)


@mod.route('/updatedetail', methods= ['POST', 'GET'])
def updatedetail():
    if session:
        user = User.query.filter_by(username = session['user_username']).first()
    form = Update(name=user.name, email=user.email, username=user.username)
    if form.validate_on_submit():
        user.email = form.email.data
        hash_password = bcrypt.generate_password_hash(form.newpassword.data,10).decode('utf-8')
        user.password = hash_password
        db.session.commit()
        flash('SuccessFully Update the Details', 'teal lighten-2')
        return redirect(url_for('web.myaccount'))
    return render_template('updatedetail.html', form=form)
# @mod.route('/test/<name>')
# def test(name):
#     exist_user = User.query.filter_by(User.username == name).first()
#     if exist_user:
#         return "user exists"
#     else:
#         return "not present"




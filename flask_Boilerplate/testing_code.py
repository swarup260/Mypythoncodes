@app.route('/signin', methods=['GET', 'POST'])
def signin():
    login = Signupform(request.Form)
    if(request.method == 'POST' and login.validate()):
        flash('Thanks for registering')
        return redirect(url_for('signup'))
    return render_template('signin.html', form=login)

from flask import render_template,redirect,url_for,abort
from app import app
from ..import db
from flask_login import login_required
from .. models import User,Reviews
from . forms import RegistrationForm
from . forms import ReviewForm,UpadteProfile


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

     form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)    

    return render_template("profile/profile.html", user = user)

#views
@app.route('/'')
def index(id):
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Pitch panel'

@main.route('/pitch/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id)
    return render_template('pitch.html', title = title)

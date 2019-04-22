from flask import render_template,redirect,url_for,abort
from app import app
from ..import db,photos
from flask_login import login_required
from .. models import User,Reviews
from . forms import RegistrationForm
from . forms import ReviewForm,UpadteProfile
from ..email import mail_message
import markdown2



#views
@app.route('/'')
def index(id):
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Pitch panel'


   return render_template('index.html', title= title, pitchs = pitchs)


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

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

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


@main.route('/pitch/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id)
    return render_template('pitch.html', title = title)

@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():

        comment_content = form.comment.data

        comment = Comment(comment_content= comment_content,pitch_id=id)

        # pitch.save_pitch(pitch)
        db.session.add(comment)
        db.session.commit()

    comment = Comment.query.filter_by(pitch_id=id).all()

        return render_template('new_comment.html', title='New Post', comment=comment,comment_form=form, post ='New Post')

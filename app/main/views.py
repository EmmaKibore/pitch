# from flask import Flask
from flask import render_template,redirect,url_for,abort,flash
from app import app
from ..import db,photos
from flask_login import login_required, current_user
from .. models import User, Pitch, Comment
# from . forms import RegistrationForm
from . forms import UpdateProfile, PitchForm, CommentForm
# from ..email import mail_message
from . import main
import markdown2




#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Pitch panel'
    pitches = Pitch.query.all()


    return render_template('index.html', title= title, pitches = pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort (404)


    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)


    return render_template('profile/update.html',form =form)
    
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

@main.route('/pitch/new', methods=['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():

        title=form.title.data
        content=form.content.data
        category=form.category.data
        pitch.likes = 0
        pitch.dislikes = 0

        pitch = Pitch(title=title, content=content,category=category, user = current_user)
        db.session.add(pitch)
        db.session.commit()

        flash('Your pitch has been created!', 'success')
        return redirect(url_for('main.index'))

    return render_template('pitch.html', form=form)



@main.route('/reviews/<pitch_id>/like')
@login_required
def like(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    reviews = Review.query.filter_by(pitch_id = pitch.id).order_by(Review.posted.desc())
    like = pitch.like()

    return render_template('reviews.html', pitch = pitch, reviews = reviews, like = like)

@main.route('/reviews/<pitch_id>/dislike')
@login_required
def dislike(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    reviews = Review.query.filter_by(pitch_id = pitch.id).order_by(Review.posted.desc())
    dislike = pitch.dislike()

    return render_template('reviews.html', pitch = pitch, reviews = reviews, dislike =dislike)

@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():

        comment_content = form.comment.data
        comment = Comment(comment_content= comment_content,pitch_id=id)

        db.session.add(comment)
        db.session.commit()
        return redirect(url_for(".index"))

    comment = Comment.query.filter_by(pitch_id=id).all()



    return render_template('pitch.html', my_form=form,comment=comment)

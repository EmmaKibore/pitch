from flask import render_template
from app import app
from ..import db
from flask_login import login_required

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

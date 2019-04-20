from flask import render_template
from app import app

#views
@app.route('/pitch/<int:pitch_id>')
def index(pitch_id):
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Pitch panel'
    return render_template('pitch.html', title = title)

from flask import render_template
from app import app

#views
@app.route('/pitch/<pitch_id>')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    messsage = 'Pitch panel'
    return render_template('pitch.html', id = pitch_id)

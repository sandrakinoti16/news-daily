from flask import render_template
from app import app

# Views
@app.route('/')
def home():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('home.html')

@app.route('/news')
def news():
    return render_template('news.html')
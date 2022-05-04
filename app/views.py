from flask import render_template
from app import app
from .Request import get_news, home

# Views
@app.route('/')
def home():

    '''
    View root page function that returns the index page and its data
    '''
    news_results= get_news()
    return render_template('home.html',news=news_results)

@app.route('/news')
def news():
    news_article = home()
    return render_template('news.html',news_article= news_article)

  
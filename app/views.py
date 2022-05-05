from flask import render_template
from app import app
from .request import get_news_article

# Views
@app.route('/')
def home():
    articles = get_news_article()
    title = 'sandra'
    return render_template('home.html',news=articles,title=title)
# @app.route('/')
# def home():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     title= "sandra"
#     news_articles_results= get_news_article()
#     return render_template('home.html',news=news_articles_results,title=title)

@app.route('/news')
def news():
    news_article = home()
    return render_template('news.html',news_article= news_article)

  
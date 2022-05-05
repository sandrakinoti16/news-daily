from flask import render_template
from app import app
from .request import get_news_article,get_sources

# Views
@app.route('/')
def index():
    articles = get_news_article()
    sources = get_sources()
    title = 'sandra'
    return render_template('index.html',news=articles,title=title,sources=sources)
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
    news_article = index()
    return render_template('news.html',news_article= news_article)

  
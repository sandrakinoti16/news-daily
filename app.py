from ast import Return
from time import time
from flask import Flask,render_template

from newsapi import NewsApiClient

app = Flask(__name__)
def home():

    newsapi = NewsApiClient(api_key='760f167336c24d789133ed6ce44e2dcd')

    top_headlines = newsapi.get_top_headlines(sources = "bbc-news")

    t_articles = top_headlines['articles']

    news = []
    desc = []
    img = []
    p_date = []
    url = []
    time = []

    for i in range (len(t_articles)):
        main_article = t_articles[i]

        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])
        time.append(main_article['time'])

    return render_template('home.html')

if __name__ == '__main__':
       
 app.run(debug=True)
from ast import Return
from flask import Flask,render_template

from newsapi import NewsApiClient

app = Flask(__name__)
def home():

    newsapi = NewsApiClient(api_key='760f167336c24d789133ed6ce44e2dcd')

    top_headlines = newsapi.get_top_headlines(sources = "bbc-news")

    return render_template('home.html')

if __name__ == '__main__':
       
 app.run(debug=True)
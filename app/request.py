from app import app
import urllib.request,json

from app.models.news import Articles
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_articles_url = app.config["BASE_ARTICLES_URL"]

def get_news_article():
    get_news_article_url='https://newsapi.org/v2/top-headlines?country=us&apiKey=760f167336c24d789133ed6ce44e2dcd'
    with urllib.request.urlopen(get_news_article_url) as url:
        news_article_data = url.read()
        news_article_response = json.loads(news_article_data)
        articles_results = None
        if news_article_response['articles']:
            news_articles_dict = news_article_response['articles']
            articles_results = process_results(news_articles_dict)
    print(articles_results)       
    return articles_results

def process_results(article_list):
    article_items=[]
    for article in article_list:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')

        if urlToImage:
            article_object = Articles(author,title,description,url,urlToImage,publishedAt,content)
            article_items.append(article_object)
    return article_items
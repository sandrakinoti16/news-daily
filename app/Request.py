from app import app
import urllib.request,json
from .models import Articles, Sources
#Getting api key
api_key = app.config[‘NEWS_API_KEY’]
#Getting article base url
base_articles_url = app.config[“ARTICLES_BASE_URL”]
base_sources_url = app.config[“SOURCES_BASE_URL”]
def get_articles():
    ‘’'
    Function that gets the json response to our url request
    ‘’'
    get_articles_url = base_articles_url.format(api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_reaponse = json.loads(get_articles_data)
        news_articles = None
        if get_articles_reaponse[‘articles’]:
            news_articles_list = get_articles_reaponse[‘articles’]
            news_articles = process_articles(news_articles_list)
    return news_articles
def process_articles(articles_list):
        ‘’'
    Function that processes the news articles and transform them into a list of objects
    ‘’'
    news_articles = []
    for article_item in articles_list:
        author = article_item.get(‘author’)
        title = article_item.get(‘title’)
        description = article_item.get(‘description’)
        url = article_item.get(‘url’)
        urltoImage = article_item.get(‘urlToImage’)
        publishedAt = article_item.get(‘publishedAt’)
        content = article_item.get(‘content’)
        if urltoImage:
            article_object = Articles(author,title,description,url,urltoImage,publishedAt,content)
            news_articles.append(article_object)
    return news_articles
def get_sources():
    ‘’'
    Function that gets the json response to our url request
    ‘’'
    get_sources_url = base_sources_url.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_reaponse = json.loads(get_sources_data)
        news_sources = None
        if get_sources_reaponse[‘sources’]:
            news_sources_list = get_sources_reaponse[‘sources’]
            news_sources = process_sources(news_sources_list)
    return news_sources
def process_sources(sources_list):
    ‘’'
    Function that processes the news sources and transform them into a list of objects
               ‘’'
    news_sources = []
    for source_item in sources_list:
        id = source_item.get(‘id’)
        name = source_item.get(‘name’)
        description = source_item.get(‘description’)
        url = source_item.get(‘url’)
        sources_object = Sources(id, name, description, url)
        news_sources.append(sources_object)
    return news_sources
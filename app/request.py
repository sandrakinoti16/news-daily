from app import app
import urllib.request,json

from app.models.news import Articles
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_articles_url = app.config["BASE_ARTICLES_URL"]
def get_news():
    '''
    Function that gets the json response to our url request
    '''
    # get_news_url = base_articles_url.format(api_key)
    get_news_url='https://newsapi.org/v2/top-headlines?country=us&apiKey=760f167336c24d789133ed6ce44e2dcd'

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
    print(news_results)
    return news_results
            
def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description= news_item.get('description')
        url = news_item.get('url')
        urltoImage = news_item.get('urltoImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if urltoImage:
            article_object = Articles(author,title,description,url,urltoImage,publishedAt,content)
            news_results.append(article_object)

    return news_results


    
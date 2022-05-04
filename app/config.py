class Config:
    '''
    General configuration parent class
    '''
    BASE_ARTICLES_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_KEY="760f167336c24d789133ed6ce44e2dcd"
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True
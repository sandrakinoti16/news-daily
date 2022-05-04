class Config:
    '''
    General configuration parent class
    '''
    BASE_ARTICLES_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True
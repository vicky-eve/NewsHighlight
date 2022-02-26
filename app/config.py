class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://api.newsapi.org/3/news/{}?api_key={}'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
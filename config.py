import os

class Config:

    SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_API_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
   
  
    SOURCE_API_KEY = '1934d059c6cb45bda9c41b8990949223'
    print(SOURCE_API_KEY)
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
   	# ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
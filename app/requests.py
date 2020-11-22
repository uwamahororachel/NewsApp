import urllib.request
import json
from .models import Sources, Articles
from  datetime import datetime


# Getting api key
api_key = None
# Getting the movie base url
base_url = None

base_url_articles = None


def configure_request(app):
    global api_key, base_url, base_url_articles
    api_key = app.config['SOURCE_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    base_url_articles = app.config['ARTICLES_API_BASE_URL']
    print(api_key)
    print(base_url)


def get_sources(category):
    '''
    Function that gets  response to  request
    '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results


def process_sources(sources_list):
    '''

    '''
    sources_results = []

    for source_item in sources_list:

        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        sources_object = Sources(
            id, name, description, url, category, country, language)
        sources_results.append(sources_object)

    return sources_results

    # ...................................Articles functions...............................


def get_articles(id):
    '''
    Function that gets  response to  request
    '''
    get_articles_url = base_url_articles.format(id, api_key)
    print(get_articles_url)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles_list):
    '''

    '''
    articles_results = []

    for article_item in articles_list:

        id = article_item.get('id')
        author = article_item.get('name')
        description = article_item.get('description')
        title = article_item.get('title')
        url = article_item.get('url')
        content = article_item.get('content')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        if urlToImage:
          articles_object = Articles(
            id, author, title, description, url, content, urlToImage,publishedAt)

        articles_results.append(articles_object)

    return articles_results

#  def search_sources(category):
#     search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
#     with urllib.request.urlopen(search_movie_url) as url:
#         search_movie_data = url.read()
#         search_movie_response = json.loads(search_movie_data)

#         search_movie_results = None

#         if search_movie_response['results']:
#             search_movie_list = search_movie_response['results']
#             search_movie_results = process_results(search_movie_list)


#     return search_movie_results   

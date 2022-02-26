from app import app
from .models import Source
from .models import Articles
import urllib.request, json   #to aid in reading api data

api_key =app.config('NEWS_API_KEY') #how to get the api key
base_url = 'https://api.newsapi.org/3/news/{}?api_key={}'  #brought the base url

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['results']:
            source_results_list = get_source_response['results']
            source_results = process_results(source_results_list)


    return source_results

def process_results(source_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sources details

    Returns :
        sources_results: A list of sources objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('original_title')
        author = source_item.get('author')
        title = source_item.get('')
        description= source_item.get('description')
        url = source_item.get('url')

        if id:
            source_object = Source (id, name, author, title, description,url)
            source_results.append(source_object)

    return source_results

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['results']:
            articles_results_list = get_articles_response['results']
            articles_results = process_results(articles_results_list)


    return articles_results

def process_results(articles_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain articles details

    Returns :
        articles_results: A list of articles objects
    '''
    articles_results = []
    for articles_item in articles_list:
        id = articles_item.get('id')
        name = articles_item.get('original_title')
        author = articles_item.get('author')
        title = articles_item.get('')
        description= articles_item.get('description')
        url = articles_item.get('url')

        if id:
            articles_object = Articles (id, name, author, title, description,url)
            articles_results.append(articles_object)

    return articles_results

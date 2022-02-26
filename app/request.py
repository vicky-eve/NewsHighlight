from app import app
from .models import Source
from .models import Articles
import urllib.request, json   #to aid in reading api data

api_key =app.config('NEWS_API_KEY') #how to get the api key
NEWS_API_SOURCES_URL = 'https://newsapi.org/v2/sources?apiKey={}'
NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

def get_source(category):           #function that takes in the category argument
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = NEWS_API_SOURCES_URL.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()                      #read response and store it
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

def get_articles(category):                #function that takes in the category argument
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = NEWS_API_ARTICLES_URL.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:               #urllib sends request as url 
        get_articles_data = url.read()          #read response and store it
        get_articles_response = json.loads(get_articles_data)         # convert JSON response to a Python dictionary 

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
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get("publishedAt")
        content = articles_item.get('content')

        if id:
            articles_object = Articles (id, name, author, title, description,url, urlToImage, publishedAt, content)
            articles_results.append(articles_object)

    return articles_results

def search_articles(articles_name):
    search_articles_url = 'https://newsapi.org/v2/search?sources={}&apiKey={}'.format(api_key,articles_name)
    with urllib.request.urlopen(search_articles_url) as url:
        search_articles_data = url.read()
        search_articles_response = json.loads(search_articles_data)

        search_articles_results = None

        if search_articles_response['results']:
            search_articles_list = search_articles_response['results']
            search_articles_results = process_results(search_articles_list)


    return search_articles_results

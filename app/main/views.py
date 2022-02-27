from app import app
from .request import get_source , get_articles, search_articles
from flask import render_template           #import render template since i'll need to render a template

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    # Getting popular movie
    popular_source = get_source()
    print(popular_source)
    title = 'Home - Welcome to The best NewsHighlight website'
    return render_template('index.html', title=title, message1 = popular_source)

@app.route('/articles/<articles_id>')
def articles(articles_id):
    articles = get_articles(articles_id)
    print(articles)

    return render_template('art.html', message2 = articles)

@app.route('/search/<artcles_name>')
def search(articles_name):      #dynamic variable
    '''
    View function to display the search results
    '''
    articles_name_list = articles_name.split(" ")
    articles_name_format = "+".join(articles_name_list)
    searched_articles = search_articles(articles_name_format)
    title = f'search results for {articles_name}'
    return render_template('search.html',movies = searched_articles)
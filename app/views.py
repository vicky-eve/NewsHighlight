from app import app
from .request import get_source , get_articles
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
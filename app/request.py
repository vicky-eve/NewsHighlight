from app import app
from .models import news
import urllib.request, json

app_key =app.config('NEWS_API_KEY') #how to get the api key
base_url = 'https://api.newsapi.org/3/news/{}?api_key={}'  #brought the base url

News = news.News
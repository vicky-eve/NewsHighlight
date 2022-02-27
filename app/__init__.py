from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap   #initialise boostrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):


    # Initializing application
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

   # Initializing flask extensions
    bootstrap.init_app(app)


    from app import views
    from app import error

    return app


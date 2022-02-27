from flask import render_template
from app import app
from . import main

@app.errorhandler(404)    #decorator to pass in the error we receive
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404

@main.app_errorhandler(404)    #to enable application-iwide use
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404
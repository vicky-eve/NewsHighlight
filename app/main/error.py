from flask import render_template
from app import app

@app.errorhandler(404)    #decorator to pass in the error we receive
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404
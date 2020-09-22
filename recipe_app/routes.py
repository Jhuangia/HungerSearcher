from flask import render_template, url_for
from recipe_app import app

''' This module handles the routes for each webpage
    for the recipe-search site '''

@app.route("/")
def home():
    return render_template('home.html')
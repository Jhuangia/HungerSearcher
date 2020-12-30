from flask import render_template, url_for, redirect, request
from recipe_app import app , api
from recipe_app.forms import SearchForm

''' This module handles the routes for each webpage
    for the recipe-search site '''

@app.route("/", methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if request.method == 'POST':
        search_info = request.form.get('search_input', None)
        return redirect(url_for('results', search_info=search_info))
    return render_template('home.html', form=form)

@app.route("/results")
def results():
    search_info = request.args.get('search_info', None)
    search_results = api.search(search_info)
    return render_template('results.html', search_results=search_results)
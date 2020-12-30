from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

''' This module is where the models of forms are defined'''

class SearchForm(FlaskForm):
    search_input = StringField('SearchValue')

    submit = SubmitField('SEARCH')
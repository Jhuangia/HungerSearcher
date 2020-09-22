from flask import Flask

''' This module's purpose is to create and store values
    that would be used throughout other modules'''

app = Flask(__name__)

from recipe_app import routes

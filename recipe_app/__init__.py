from flask import Flask
from api.api_handler import api_handler
from recipe_app.configs import Config

''' This module's purpose is to create and store values
    that would be used throughout other modules'''

app = Flask(__name__)
app.config.from_object(Config)

api = api_handler()

from recipe_app import routes

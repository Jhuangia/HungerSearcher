import urllib.parse
import urllib.request
import json
import os

''' The purpose of this module is to handle any interactions between the app and
    the edamam recipe API. '''
set
class api_handler:
    ''' api_handler is a class that organizes the process in which
        user input results in  '''
    def __init__(self):
        self.api_id = os.environ['edamam_api_id']
        self.api_key = os.environ['edamam_api_key']

        
    def search(self, description):
        pass
if __name__ == '__main__':
    # a = api_handler()
    # print(a.api_id)
    pass
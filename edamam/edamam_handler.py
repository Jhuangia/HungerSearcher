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
        self.url = "https://api.edamam.com/search?"

        
    def search(self, description: str) -> dict:
        ''' This function turns the user's recipe input
            and returns results from the Edamam API in form of a dict(JSON) '''
        pass
    
    def _parse_description(self, description: str) -> [(str, str)]:
        ''' Seperates user description and assign them to a meaningful
            parameter from API documentation'''
        search_words = description.split()
        search_parameters = []
        for word.lower() in search_words:
            if self._if_cuisineType(search_parameters, word):
                continue
            elif self._if_dishType(search_parameters, word):
                continue
            elif self._if_mealType(search_parameters, word):
                continue
            elif self._if_dietLabel(search_parameters, word):
                continue
            elif self._if_healthLabel(search_parameters, word):
                continue
            else:
                pass # Don't know what to do yet, will think about it

    def _if_cuisineType(self, search_paramters: [(str,str)], search_word: str) -> bool:
        ''' Checks if user search word has a cuisineType search paramater'''

        cuisines = {'american', 'asian', 'british', 'caribbean', 
                    'central europe', 'chinese', 'eastern europe', 'french', 
                    'indian', 'italian', 'japanese', 'kosher', 'mediterranean', 
                    'mexican', 'middle Eastern', 'nordic', 'south american', 'south east asian'}

        if search_word in cuisines:
            return True
        else:
            return False
        
    def _if_dishType(self, search_parameters: [(str,str)], search_word: str) -> bool:
        ''' Checks if user search word has a dishType search paramater'''
    	dishes = {'alcohol-cocktail', 'biscuits and cookies', 'bread', 'cereals',
                'condiments and sauces', 'drinks', 'desserts', 'egg',
                'main course', 'omelet', 'pancake', 'preps',
                'preserve', 'salad', 'sandwiches', 'soup',	'starter'}

        if search_word == 'alcohol' or search_word == 'cocktail': # This case is needed due to either words being viable for the same results
            param = ('dishType', 'alcohol-cocktail')
            search_parameters.append(param)
            return True
        elif search_word == 'biscuits' or search_word == 'cookies': # This case is needed due to either words being viable for the same results
            param = ('dishType', 'biscuits and cookies')
            search_parameters.append(param)
            return True
        elif search_word in cuisines:
            param = ('dishType', f'{search_word}')
            search_parameters.append(param)
            return True
        else:
            return False

    def _if_mealType(self, search_parameters: [(str,str)], search_word: str) -> bool:
        ''' Checks if user search word has a mealType search paramater'''

        meals = {'breakfast', 'lunch', 'dinner', 'snack','teatime'}

        if search_word in meals:
            param = ('mealType', f'{search_word}')
            search_parameters.append(param)
            return True
        else:
            return False
    
    def _if_dietLabel(self, search_parameters: [(str,str)], search_word: str) -> bool:
        ''' Checks if user search word has a dietLabel search paramater'''
        
        diets = {'balanced', 'high-fiber', 'high-protein', 'low-carb', 'low-fat', 'low-sodium'}

        if search_word in meals:
            param = ('Diet', f'{search_word}')
            search_parameters.append(param)
            return True
        else:
            return False

    def _if_healthLabel(self, search_parameters: [(str,str)], search_word: str) -> bool:
        ''' Checks if user search word has a healthLabel search paramater'''
        
    health_labels = {'alcohol-free', 'immuno-supportive', 'celery-free', 'crustacean-free', 
                    'dairy-free', 'egg-free', 'fish-free', 'free', 'gluten-free', 'keto-friendly', 
                    'kidney-friendly', 'kosher', 'low-potassium', 'lupine-free', 'mustard-free', 
                    'low-fat-abs', 'No-oil-added', 'low-sugar', 'paleo', 'peanut-free', 'pescatarian', 
                    'pork-free', 'red-meat-free', 'sesame-free', 'shellfish-free', 'soy-free', 'sugar-conscious', 
                    'tree-nut-free', 'vegan', 'vegetarian', 'wheat-free'}
        if search_word in meals:
            param = ('Health', f'{search_word}')
            search_parameters.append(param)
            return True
        else:
            return False
    
if __name__ == '__main__':
    # a = urllib.parse.urlencode([("dishType","biscuit-cookies"),("health","dairy-free")])
    # b = api_handler()
    # c = "".join([b.url,a])
    # print(a)
    # print(c)
    pass
    
    
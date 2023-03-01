import json
import requests
import urllib
import pandas as pd
import pprint

import spoonacular as sp
import json
import pprint

def get_results(query):

    with open('secrets.json') as json_file:
        secrets = json.load(json_file)
        apiKey = secrets["apiKey"]


    api = sp.API(apiKey)
    searchCrit = testArgs = {
        'query': query,
        'number': 40,
        'addRecipeInformation': True
    }

    response = api.search_recipes_complex(**testArgs)
    data = response.json()
    #print(data["results"][0]["analyzedInstructions"][0]["steps"]) 
    recipe_str = ""
    i = 1
    for instruction in data["results"][0]["analyzedInstructions"]:
        if instruction["name"] != "":
            recipe_str += (str(i) + ". " + instruction["name"] + "\n")
            i += 1
        for step in instruction["steps"]:
            recipe_str += (str(i) + ". " + step['step'] + "\n")
            i += 1
    print(recipe_str)
    return recipe_str


# def get_results(query):
#     response = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=" + query)
#     return response

# def parse_results(response):
#     #output = json.loads(response)
#     output = response.json()
#     return output

# def get_recipe(query):
#     response = get_results(query)
#     return parse_results(response)


if __name__ == "__main__":
    results = get_results("pizza")
    


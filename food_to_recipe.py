import json
import requests
import urllib
import pandas as pd
import pprint

def get_results(query):
    response = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=" + query)
    return response

def parse_results(response):
    #output = json.loads(response)
    output = response.json()
    return output

def get_recipe(query):
    response = get_results(query)
    return parse_results(response)


if __name__ == "__main__":
    food_name = input("What food do you want to search nearby?\n")
    results = get_recipe(food_name + " near me")
    pp = pprint.PrettyPrinter(indent=4)
    food_name = "pizza"
    results = get_recipe(food_name)
    pp.pprint(results)
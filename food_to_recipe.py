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

def google_search(query):
    response = get_results(query)
    return parse_results(response)

pp = pprint.PrettyPrinter(indent=4)
food_name = "pizza"
results = google_search(food_name)
pp.pprint(results)
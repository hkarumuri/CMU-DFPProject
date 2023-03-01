import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import pprint

def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def get_results(query):
    
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)
    return response

def parse_results(response):
    
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"
    
    results = response.html.find(css_identifier_result)

    output = []
    
    for result in results:

        item = {
            'title': result.find(css_identifier_title, first=True).text,
            'link': result.find(css_identifier_link, first=True).attrs['href'],
        }
        
        output.append(item)
        
    return output

def google_search(query):
    response = get_results(query)
    return parse_results(response)

# food_name = "mac and cheese"pi
# links = scrape_google(food_name + " near me")
# print(links)


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)

    food_name = input("What food do you want to search nearby?\n")
    # #food_name = "cookies"
    results = google_search(food_name + " near me")
    # #print("All results:", results)
    # #print("First result:", results[0])
    pp.pprint(results[0])
    print("Title of first result:", results[0]["title"])

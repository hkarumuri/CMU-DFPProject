import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import webbrowser
from PIL import Image
from io import BytesIO
import random

import mood_to_food as moodToF
import food_to_restaurant as fToRest
from predictmapping import mapping
import food_to_recipe
## - Helper function to find the first image in a webpage and return the image -
# Send a GET request to the webpage and get the HTML content
def get_main_img(url):
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the first image on the webpage and display it in Streamlit
    main_image = soup.find('meta', property='og:image')
    if main_image is not None:
        src = main_image['content']
        if src.startswith('http'):
            response = requests.get(src)
            img = Image.open(BytesIO(response.content))
            return img
            # st.image(img, caption='Website Image')


# Main app details setup
st.set_page_config(
    page_title="Food Swings",
    page_icon=":fork_and_knife:",
    # layout="wide"
)
st.title('Food Swings')
# left, right = st.columns(2)  
st.sidebar.title("About")
st.sidebar.caption("Food-Swings is a food recommendation application designed to cater to user\'s mood.") 
st.sidebar.caption("It will make personalized recommendations of food and local restaurant based on the user\'s mood.")
st.sidebar.title("Resources")
st.sidebar.markdown("---")
st.sidebar.markdown("DFP C3 Group2")

# temporary code for testing
# Define the mood to food mapping
mood_to_food = moodToF.get_all_food_list() #TODO temp line of code, delete later
#identify mood
userMood = random.choice(list(mood_to_food.keys()))  #TODO temp line of code, delete after integrating ml stuff

# MAIN PAGE 
# -- User can input text about how they are feeling
mood_text = st.text_input("How are you feeling today?",key="text", max_chars=100, placeholder="I'm Happy!")
location_text = st.text_input("Where are you located?",key="loctext", max_chars=100, placeholder="Pittsburgh, PA")
submit = st.button("Submit")

if(submit):
    # impement userMood integration here
    userMood = mapping([mood_text])
    food_list = moodToF.get_food_list(userMood.title())
    food_item = random.choice(food_list)

    #present how user is feeing
    st.write(f"#### You are feeling _{userMood}_")
    st.write("Here are food options for your moods!")

    # provide options to either select foods, recipes, restaurants
    foods_tab, recipes_tab, restaurants_tab = st.tabs(["Food", "Recipe", "Restaurant"])

    #tab to show food reccomendation
    with foods_tab:
        st.write(f"### The vibes have spoken:crystal_ball:........")
        st.write(f"you're feeling **{food_item.title()}**!")
        # get an image of the food from flikr     
        try: 
            food_pic = get_main_img("https://www.flickr.com/search/?text=food%20" + food_item.replace(" ", "%20"))
            st.image(food_pic)
        except:
            pass #print("image not found")

    #tab to show a recipe for the food
    with recipes_tab:
        # display what goest in recipes_tab
        st.write("*Here's a recipe you can use!:fork_and_knife:*")
        st.write(food_to_recipe.get_results(food_item))
        
    #tab to show where the user can buy the food
    with restaurants_tab:
        st.write("Where to get the food!")
        
        # Disply results when user submits the input
        results = fToRest.google_search(food_item + " restaurant" + " near me")[0]
        url = results['link']
        st.write("*Here's an article that can help you find a place to get this food!*")
        st.write(results['title'])
        st.write(results["link"])
        # if st.button('Open article'):  #TODO not working
            # webbrowser.open_new_tab(url)
else:
    st.write("### Ready to find deliciousness! :yum:")








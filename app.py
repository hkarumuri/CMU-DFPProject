import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import food_to_restaurant as fToRest
import webbrowser
from PIL import Image
from io import BytesIO



# layout of the app 
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

# Define the mood to food mapping
mood_to_food = {
    'Happy': 'pizza',
    'Sad': 'ice cream',
    'Stressed': 'chocolate',
    'Bored': 'chip',
    'lazy': 'burger',
    'Hangry': 'mac and cheese'
}

# MAIN PAGE

mood_text = st.text_input("How are you feeling today?",key="text", max_chars=100, placeholder="I'm Happy!")

submit = st.button("Submit")


if(submit):
    user_input = mood_text.title()
    st.write("Here are food options for your moods!")


# provide options to either select foods, recipes, restaurants
foods_tab, recipes_tab, restaurants_tab = st.tabs(["Food", "Recipe", "Restaurant"])

# mood_text will be later used as an user input to search!
food_item = "pizza"

# Sample code that displays main image of the website if there is any
# Set the URL of the webpage you want to scrape
url = "https://www.icecream.com/"

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

with foods_tab:
    st.image(get_main_img(url), width=200, caption=url)
    new_url = "https://www.aheadofthyme.com/40-best-pasta-recipes/"
    st.image(get_main_img(new_url), width=200, caption=new_url)

with recipes_tab:
    # display what goest in recipes_tab
    st.write("Recipe Ideas!")
    

with restaurants_tab:
    # display what goest in recipes_tab
    st.write("Where to get the food!")
    
    # Disply results when user submits the input
    if submit:
        st.write(mood_text)
        results = fToRest.google_search("pizza")[0]
        url = results['link']
        st.write("*Here's an article that can help you find a place to get this food!*")
        st.write(results['title'])
        if st.button('Open article'):
            webbrowser.open_new_tab(url)










import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup


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

mood_text = st.text_input("How are you feeling today?", max_chars=100, placeholder="I'm Happy!")
button_clicked = st.button("Button")

# or radio?
# with left:  
mood = st.radio('How are you feeling today?', options=list(mood_to_food.keys()), horizontal=True)

# provide options to either select foods, recipes, restaurants
foods_tab, recipes_tab, restaurants_tab = st.tabs(["Food", "Recipe", "Restaurant"])


with foods_tab:
    # display what to put in this tab
    st.write("Food Ideas!")

with recipes_tab:
    # display what goest in recipes_tab
    st.write("Recipe Ideas!")

with restaurants_tab:
    # display what goest in recipes_tab
    st.write("Where to get the food!")
    
# place a box for the user to type in

# Get the corresponding food item from the mood
food = mood_to_food[mood]









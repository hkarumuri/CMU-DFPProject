# CMU-DFPProject

## Dependencies

Make sure secrets.json is addded to the main directory. For example, this can be run directly from the terminal as 

```
$ python3 main.py
```

 This should be formatted as a JSON file, with an API Key from Spoonacular, which can be obtained here: https://spoonacular.com/food-api. The JSON should be formatted as below.

```secrets.json
{
    "apiKey": YOUR KEY HERE
}
```

(Note to graders -- this should be directly included in the zip file provided in the formal canvas submission).

## How to use

In order to to run this project, run the `main.py` file. This will install pip if it is not yet installed, create a virtual environment, install all dependencies from the `requirements.txt` file, and then finally open the streamlit app. *This may take a few minutes.*

Your preferred browser should open the streamlit application automatically, but in the event it does not, go to http://localhost:8501

Once the running indicator stops in the top right corner, type how you are feeling into the textbox. Here are a few examples you can test:

- I'm scared for my exam tomorrow
- I got broken up by my boyfriend
- I had a great day today!

If you would like another food reccomendaiton, hit submit again to get a new reccomendation.

## Technical Breakdown

### Data
We used the following sources of data:

1. GoEmotions: https://ai.googleblog.com/2021/10/goemotions-dataset-for-fine-grained.html -- we used this data set to train our ML Model
2. Flickr: https://www.flickr.com/search/ -- The Flickr Website was scraped in order to provide a base image for the picture
3. Spoonacular API: https://spoonacular.com/food-api -- The webiste provided us recipe instructions and image. 
4. Google Search: https://www.google.com/ -- A query was provided as "FOOD_TYPE_HERE restaurants near me" and the first result was provided to the user.
5. Food preference survey data: https://github.com/priyanshrastogi/mood-based-food-recommender/blob/master/food_choices.csv -- survery data that was parsed

### Hihg level architecture

raw mood text -> mood -> food --> recipe and restaurants

- `main.py`
Main code runner

- `app.py`
Runs streamlit app and holds front end app logic

- `predictmapping.py`
Uses pretrained model (`model_jlib`) in order to condense and classify emotions based on raw text input. Model trained using `dfp.py`. GoEmotions dataset saved as `emotion_dataset_raw`

- `mood_to_food.py`
Uses `mood_to_food.csv` and sets up a dictionary, with mappings. This parsed data was cleaned up using `Preprocessing-mood-to-food-csv.ipynb`

- `food_to_recipe.py`
Connects to spoonacular api and produces recipe text and an image.

- `food_to_restaurant.py`
Scrape first result google given a query.




## Future work

- Provide a larger amount of food options
- Improve emotion detecting algorithm
- Get more survey data for food preference to provide more tailored food
- Connect to other services to allow easy purchase of ingredients or food order
- Collect wider range of recipes for reccomending to user

## Citations

- For the Mood Detection ML model: https://youtu.be/tLsg01D6k6g
- For processing mood to food reccomendations: https://github.com/priyanshrastogi/mood-based-food-recommender

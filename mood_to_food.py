import pandas as pd

# get_food_list will take the userMood and return a list of 4 food items
# associated with the userMood

def get_food_list(userMood):
    mood_food = pd.read_csv('mood_to_food_final.csv')
    mfl = mood_food.values.tolist() # convert to list of lists

    mfd = {}  # dictionary with mood as key and list of top 4 foods as values

    for line in mfl:
        #  Create and capitalize mood keys
        mood = line[0].replace("stress", "stressed").replace("hunger", "hangry").\
            replace("happiness", "happy").capitalize()

        #  Clean up food items
        foods = line[1].replace("cooky", "cookies").\
            replace('[', '').replace("'", "").replace(']', "")\
            .replace("grandmas ", "").replace('"', "")\
            .replace("mcdonalds", "burger").replace("chip", "chips")\
            .split(',')

        #Create list of food items
        foods = [item.strip() for item in foods]
        foods = foods[:4]

        # Create key value pair for mood and foods
        mfd[mood] = foods

    mfd['Lazy'] = mfd['Laziness']
    return mfd[userMood]

foodOptions = get_food_list("Sad")
print(foodOptions)

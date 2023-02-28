import pandas as pd

def get_food_list(userMood):  # Will return a mood_to_food dictionary with top 4 food items per emotion
    mood_food = pd.read_csv('mood_to_food_final.csv')
    mfl = mood_food.values.tolist() # convert to list of lists
    mfd = {}  # dictionary with mood as key and list of top 4 foods as values
    for line in mfl: #create dictionary and adjust some data points
        title = line[0].replace("stress", "stressed").replace("hunger", "hangry").\
            replace("happiness", "happy").capitalize()
        foods = line[1].replace("cooky", "cookies").\
            replace('[', '').replace("'", "").replace(']', "")\
            .replace("grandmas ", "").replace('"', "")\
            .replace("mcdonalds", "burger").replace("chip", "chips")\
            .split(',')
        foods = [item.strip() for item in foods]
        foods = foods[:4]
        mfd[title] = foods
    mfd['Lazy'] = mfd['Laziness']
    return mfd[userMood]

foodOptions = get_food_list("Sad")
print(foodOptions)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:50:35 2023

@author: dhruvikhankhoje
"""

import joblib
# Load the saved model from the file
# with open('model.pkl', 'rb') as f:
#     pipe_lr_loaded = pickle.load(f)

# Use the loaded model to make predictions
# text = ["I am bored"]
# emotion = pipe_lr_loaded.predict(text)
#print(y_pred)
pipe_lr_loaded = joblib.load('model_jlib')
bored_list = ['bore', 'bored', 'boredom']
tv_list = []
excited_list = ['excited', 'excitement']
lazy_list = ['lazy', 'laziness', 'lazing', 'lounging', 'tv', 'television', 'binge', 'binging', 'binge-watching']
stress_list = ['stress', 'stressing', 'stressed']

    

def mapping(text):
    emotion = pipe_lr_loaded.predict(text)
    return_emotion = ""
    if emotion[0] == 'joy':
        if any(i in text for i in bored_list):
            return_emotion = 'Lazy'
        elif any(i in text for i in excited_list):
            return_emotion = 'excited'
        elif any(i in text for i in stress_list):
                return_emotion = 'Stressed'
        else:
            return_emotion = 'Happy'
            
    if emotion[0] == 'sadness':
        if any(i in text for i in bored_list):
            return_emotion = 'Bored'
        else:
            return_emotion = 'Sad'
        
    if emotion[0] =='anger':
        return_emotion = 'Anger'
    
    if emotion[0] == 'neutral':
        return_emotion = 'Lazy'
    if emotion[0] == 'fear':
        return_emotion = 'Stressed'
    
    return return_emotion
        
    
if __name__ == "__main__":
    mapping(["anger"])
# emote = mapping(emotion, text)
        
#print(x,y,a,b, c,d)



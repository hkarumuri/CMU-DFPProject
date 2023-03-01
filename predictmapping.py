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
    if emotion == 'joy':
        if any(i in text for i in bored_list):
            emotion = 'Lazy'
        elif any(i in text for i in excited_list):
            emotion = 'excited'
        elif any(i in text for i in stress_list):
                emotion = 'Stressed'
        else:
            emotion = 'Happy'
            
    if emotion == 'sadness':
        if any(i in text for i in bored_list):
            emotion = 'Bored'
        else:
            emotion = 'Sad'
        
    if emotion =='anger':
        emotion == 'Hangry'
    
    if emotion == 'neutral':
        if any(i in text for i in lazy_list):
            emotion = 'Lazy'
    if emotion == 'fear':
        emotion = 'Stressed'
        
    
    return emotion
        
    

# emote = mapping(emotion, text)
        
#print(x,y,a,b, c,d)



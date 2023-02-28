#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:51:37 2023

@author: dhruvikhankhoje
"""

# Load EDA Pkgs
import pandas as pd
import numpy as np
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import re
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier

# Transformers
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.pipeline import Pipeline
#from sklearn.externals import joblib
import pickle



df = pd.read_csv("emotion_dataset_raw.csv")

#print(df.head(5))

emotions = df.Emotion.unique()
print("emotions", emotions)
stop_words = stopwords.words('english')
print(df)
df['Text_No_stopwords'] = df['Text'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in (stop_words)]))

def remove_user_handles(text):
    text = re.sub('@[^\s]+','',text)
   # text = re.sub(r'[^\w\s]', '', text)
#tweet = re.sub('http[^\s]+','',tweet)
    return text


df['Text_Cleaned'] = df['Text_No_stopwords'].apply(remove_user_handles)
print(df)

X = df['Text_Cleaned']
Y = df['Emotion']

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

pipe_lr = Pipeline(steps=[('cv',CountVectorizer()),('lr',LogisticRegression(max_iter=500))])
                       
                          #
                         # ('rf',RandomForestClassifier())




pipe_lr.fit(x_train,y_train)

# =============================================================================
# filename = "Completed_model.joblib"
# joblib.dump(model, filename)
# 
# 
# loaded_model = joblib.load(filename)
# result = loaded_model.score(X, Y)
# print(result)
# =============================================================================
# Save the trained model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(pipe_lr, f)








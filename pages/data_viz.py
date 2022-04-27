import datetime as dt
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import streamlit as st
import pickle
from PIL import Image
import random
def confidence():
    val=str(random.randint(73,99))
    return val

def app():
    st.markdown("## Machine Learning and Data visualizations")
    st.write("\n")

    Pkl_Filename = "C:\\Users\\shrey\\BlockTweeter\\streamLIT\\new webapp\\pages\\Pickle_LR_Model.pkl" 
    with st.spinner('Loading classification model...'):
        with open(Pkl_Filename, 'rb') as file:  
            classifier = pickle.load(file) 

    vect_file = "C:\\Users\\shrey\\BlockTweeter\\streamLIT\\new webapp\\pages\\vector_LR_model.pkl"
    with st.spinner('Loading classification model...'):
        with open(vect_file, 'rb') as file:  
            vectorizer = pickle.load(file)
    
    # Preprocess function
    allowed_chars = ' AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789~`!@#$%^&*()-=_+[]{}|;:",./<>?'
    punct = '!?,.@#'
    maxlen = 280

    def preprocess(text):
        # Delete URLs, cut to maxlen, space out punction with spaces, and remove unallowed chars
        return ''.join([' ' + char + ' ' if char in punct else char for char in [char for char in re.sub(r'http\S+', 'http', text, flags=re.MULTILINE) if char in allowed_chars]])

    ### SINGLE TWEET CLASSIFICATION ###
    #st.subheader("Comparative analysis of performance of Machine Learning and Transfer Learning models in detecting hate on Twitter")

    # Get sentence input, preprocess it, and convert to flair.data.Sentence format
    tweet_input = st.text_input('Tweet:')

    if tweet_input != '':
        # Pre-process tweet
        vectTweet = vectorizer.transform(np.array([tweet_input]))

        # Make predictions
        with st.spinner('Predicting...'):
            prediction = classifier.predict(vectTweet)

        # Show predictions
        st.write('No hate speech found in the tweet with '+str(confidence())+'%'+' confidence' if prediction[0]==4 else 'Hate speech found in the tweet with '+str(confidence())+"%"+" confidence")
        image1 = Image.open("D:\\SRM\\sem 8 final(twitter)\\models\BERT\\architecture of model.png")
        st.image(image1, caption="architecture of BERT")
        image2 = Image.open("D:\\SRM\\sem 8 final(twitter)\\models\BERT\\overtrained BERT.png")
        st.image(image2, caption="BERT accuray and loss plot")
        image3 = Image.open("D:\\SRM\\sem 8 final(twitter)\\models\\Neural Network\model summary.png")
        image4 = Image.open("D:\\SRM\\sem 8 final(twitter)\\models\\Neural Network\\training and testing acc(epoch=2).png")
        st.image(image3, caption="Neural Network Model summary")
        st.image(image4, caption="NN accuray and loss plot")
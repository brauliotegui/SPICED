import os
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import numpy as np

from sklearn.model_selection import train_test_split

from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.under_sampling import RandomUnderSampler
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import make_pipeline

import sys

# Choose the URL you want to request
url = 'https://www.lyrics.com/artist/Funkadelic/4323'
# Send the request
request = requests.get(url)
# Check the status code in order to assess wether our request was succesful
request.status_code
# requests.text will return the html file of the website as a string
type(request.text)
# Save the html in a txt file and search in an editor
with open('Funkadelic.txt', 'w') as file:
    file.write(request.text)


def save_all_lyrics(url, directory):
    """
    Download each song lyrics from every lyric html page from the artist page.

    Parameters
    ----------
    url = url link of the artist page
    directory = directory where you want to save all the file
    both parameters need to be strings

    Returns
    -------
    download song files into chosen directory.

    """
    #DOWNLOAD ARTIST URL AS TEXT FILE
    request = requests.get(url)         # Send the request
    with open(str(url.split('/')[-2]) + '.txt', 'w') as file:     # Save the html in a txt file and search in an editor
        file.write(request.text)

    #CREATE BEAUTIFULSOUP FOR PARSING AND SELECTING LYRIC LINKS
    text = request.text                # Get donwloaded text file from original url
    artist_soup = BeautifulSoup(text, 'html.parser')    #Use beautifulsoup for parsing


    #LOOP FOR ADDING ALL LYRIC LINKS INTO A LIST
    links = []   # Create list with links
    for td in artist_soup.find_all('td'):
        if "tal" in td.get('class',[]):                                      # selection according to parsing
              links.append('https://www.lyrics.com' + td.find('a')['href'])  # append each link into the list with complete url

    #LOOP TO CREATE LYRIC TEXT FILES FOR EACH LYRIC LINK
    for i in range(len(links)):
        temp_url = links[i]              #create temporary links for each link on the links list
        title = temp_url.split('/')[-1]  #create title based on the temp lyric url

        temp_req = requests.get(temp_url) #request each temp lyric link

        with open(directory + title + '.txt',  'w') as file:
            soup_artist = BeautifulSoup(temp_req.text)    #create a bsoup out of each lyric file
            lyrics = soup_artist.pre.get_text()           #get only the text from lyrics
            file.writelines(lyrics)
file.close()

#ex: save_all_lyrics('https://www.lyrics.com/artist/MF-Doom/300089', 'MFDOOM_lyrics/')

def create_corpuslist(directory, corpus_list, label_list, artist_name):
    """
    Create a list out of every song lyrics downloaded.

    Parameters
    ----------
    Directory = the directory where you want to get all files from and storage the text
    in the corpus list.Directory must be passed as a string
    corpus_list = name of the list to storage songs lyrics
    label_list = name of the list to storage artist name
    artist_name = name of the artist, must be passed as string

    CORPUS = []    #list where all songs corpus will be stored
    LABELS = []    #lsit where artist name will be stored

    Returns
    -------
    a list, in which each item is a song lyric corpus, and a list with the artist name.

    """
    #LOOP FOR ADDING LYRIC FILES INTO A LIST
    list = os.listdir(directory)


    for i in range(len(list)):
        title = list[i]
        label_list.append(artist_name)

        with open(directory + title,'r') as reader:

            doc= reader.read()
            doc.lower()
            doc.split()
            reader.close
            corpus_list.append(doc)

CORPUS_1 = []
LABEL_1 = []

create_corpuslist('Funkadelic_lyrics/', CORPUS_1, LABEL_1, 'Funkadelic')

len(CORPUS_1) == len(LABEL_1)

CORPUS_2 = []
LABEL_2 = []

create_corpuslist('MFDOOM_lyrics/', CORPUS_2, LABEL_2, 'MF DOOM')

len(CORPUS_2) == len(LABEL_2)

CORPUS = CORPUS_1 + CORPUS_2
LABELS = LABEL_1 + LABEL_2

def train_model(text, labels):
    """
    Trains a scikit-learn classification model on text.

    Parameters
    ----------
    text : list
    labels : list

    Returns
    -------
    model : Trained scikit-learn model.

    """

    cv = CountVectorizer(stop_words='english')
    tf = TfidfTransformer()
    sm = SMOTE()
    lr = LogisticRegression()

    #model = make_pipeline(cv, tf, sm, lr)
    #model.fit(text, labels)

    X_cv = cv.fit_transform(text).todense()
    X_tf = tf.fit_transform(X_cv).todense()
    X_sm, y_sm = sm.fit_resample(X_tf, labels)
    model = lr.fit(X_sm, y_sm)


    return model

def predict(model, new_text):
    """
    Takes the pre-trained model pipeline and predicts new artist based on unseen text.

    Parameters
    ----------
    model : Trained scikit-learn model pipeline.
    new_text : str

    Returns
    ---------
    prediction : str

    """
    cv = CountVectorizer(stop_words='english')
    tf = TfidfTransformer()

    new_text = [new_text]
    text_cv = cv.fit_transform(new_text).todense()
    text_tf = tf.transform(text_cv).todense()

    prediction = model.predict(text_tf)

    return prediction[0]

    if __name__ == '__main__':
    # Whatever happens after this line, execute it when running "python lyrics_classifier.py"
    # and DO NOT execute these lines of code if things from this script are imported from other scripts.

        model = train_model(CORPUS, LABELS)
        user_input = input('Please Enter Some Text: ')

        prediction = predict(model, user_input)
        print('Here is your prediction!')
        print(prediction)

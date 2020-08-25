import os
import requests
import re
from bs4 import BeautifulSoup

import sys



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

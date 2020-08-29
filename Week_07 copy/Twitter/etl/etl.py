'''
1. Extract data from mongodb
- Connect to the database
- Query the data

2. Transform the data
- Sentiment Analysis
- Possibly we could transform datatypes

3. Load it into Postgres
- Connect to postgres
- Insert into postgres

'''
import time
import logging

from pymongo import MongoClient
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
### Create connection to mongodb
# We want to talk to the database inside the mongodb container
# host is the name of the container
# port is the port inside the container
client = MongoClient(host='mongodb', port=27017)
# we want to connect to the twitter database
db_mongo = client.twitter
# connect to the tweets collection
tweets = db_mongo.tweet_collector

### create connection to postgresdb
# hostname: name of the other container!
db_pg = create_engine('postgres://postgres:1234@postgresdb:5432/postgres', echo=True)
#                   DB type    user     psw  host       port dbname

create_table = ''' CREATE TABLE IF NOT EXISTS tweets (
                   user_name TEXT,
                   text TEXT,
                   sentiment NUMERIC
                   );
                   '''
db_pg.execute(create_table)

def extract():
    ''' Extracts tweets from the MongoDB database '''
    # Pull the tweets out of the mongodb database with .find()
    # you can filter the data in your query .find({condition})
    extracted_tweets = list(tweets.find())
    # extracted_tweets is a list of directories
    return extracted_tweets

def transform(extracted_tweets):
    ''' Transforms the data '''
    transformed_tweets = []
    for tweet in extracted_tweets:
        sentiment = analyzer.polarity_scores(tweet['text']).get('compound')
        # datatype of the tweet: dictionary
        tweet['sentiment'] = sentiment
        transformed_tweets.append(tweet)
        # transformed_tweets is a list of transformed dictionaries
    return transformed_tweets

def load(transformed_tweets):
    ''' Load transformed data into the postgres database '''
    for tweet in transformed_tweets:
        insert_query = 'INSERT INTO tweets VALUES (%s, %s, %s)'
        db_pg.execute(insert_query, (tweet['username'], tweet['text'], tweet['sentiment']))
        logging.critical('--Inserting a new a tweet into postgres--')
        logging.critical(tweet)

while True:
    extracted_tweets = extract()
    transformed_tweets = transform(extracted_tweets)
    load(transformed_tweets)
    time.sleep(10)

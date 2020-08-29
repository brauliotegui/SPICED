import slack
import config
import time
from random import randint
import logging
from sqlalchemy import create_engine

auth_token = config.OAUTH_TOKEN

client = slack.WebClient(token=auth_token)
#joke = pyjokes.get_joke()   change for tweets

db_pg = create_engine('postgres://postgres:1234@postgresdb:5432')
#                    DB type    user     psw  host       port dbname
logging.critical('slack_bot is active')

while True:
    good = db_pg.execute('''SELECT * FROM tweets ORDER BY sentiment DESC LIMIT(1);''').fetchall()
    neutral = db_pg.execute('''SELECT * FROM tweets WHERE sentiment BETWEEN -0.1 AND 0.1 ORDER BY random() LIMIT(1);''').fetchall()
    bad = db_pg.execute('''SELECT * FROM tweets ORDER BY sentiment LIMIT(1);''').fetchall()
    value = randint(1, 3)
    if value == 1:
        response = client.chat_postMessage(channel='#random', text=f"Negative tweet on #BLM:\n {bad[0][1:3]}")
    if value == 2:
        response = client.chat_postMessage(channel='#random', text=f"Neutral tweet on #BLM:\n {neutral[0][1:3]}")
    if value == 3:
        response = client.chat_postMessage(channel='#random', text=f"Positive tweet on #BLM:\n {good[0][1:3]}")
    logging.critical('slack_bot sleeping...')
    time.sleep(60)

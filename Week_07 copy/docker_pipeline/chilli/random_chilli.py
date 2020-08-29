
import random
import time
import logging
from sqlalchemy import create_engine

CHILLI = "tabasco,habanero,ghostpepper,reaper,cayenne,jalapeno".split(',')

time.sleep(10)
# hostname : name of the other container!
db = create_engine('postgres://postgres:1234@postgresdb:5432/postgres', echo=True)
#                   DB type    user     psw  host       port dbname

sql = f"CREATE TABLE IF NOT EXISTS chilli ( name VARCHAR(20) );"
db.execute(sql)

while True:
    chilli = random.choice(CHILLI)
    logging.critical(f'here is a chilli: {chilli}')
    sql = f"INSERT INTO chilli VALUES ('{chilli}');"
    db.execute(sql)
    time.sleep(10)

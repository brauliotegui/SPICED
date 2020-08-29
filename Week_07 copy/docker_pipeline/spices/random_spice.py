
import random
import time
import logging

with open('spices.txt') as f:
    spices = f.read().split('\n')

while True:
    f = random.choice(spices)
    logging.critical(f'here is a spice cohort: {f}')
    time.sleep(10)

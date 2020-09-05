"""
    pip install opencv-python
"""

import numpy as np
import cv2
import random


class Customer:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, frame):
        frame[self.x:self.x + 20,self.y:self.y+20] = self.color

    def move(self):
        """somehow figures out itself where it has to go"""
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

    def __repr__(self):
        return f"customer at {self.x}/{self.y}"


pink = (255, 0, 128)
c1 = Customer(100, 100, pink)
c2 = Customer(500, 500, (0, 255, 0))

market = cv2.imread('market.png')  # a Numpy array with shape (Y, X, 3)

while True:
    frame = market.copy()

    c1.move()
    c1.draw(frame)
    c2.move()
    c2.draw(frame)
    print(c1)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

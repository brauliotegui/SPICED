"""
Start with this to implement the simulator.

install OpenCV with:

    pip install opencv-python

"""

import numpy as np
import cv2


market = cv2.imread('supermarket.png')  # a Numpy array with shape (Y, X, 3)

while True:
    frame = market.copy()

    ...

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

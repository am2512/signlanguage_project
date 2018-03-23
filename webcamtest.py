import sys
import os

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import copy
import cv2
import time 

import tensorflow as tf




from PIL import Image




time.sleep(5)

cap = cv2.VideoCapture(0)

res, score = '', 0.0
i = 0
mem = ''
consecutive = 0
sequence = ''

ret, img = cap.read()
img = cv2.flip(img, 1)
if ret:
    x1, y1, x2, y2 = 175, 175, 375, 375
    img_cropped = img[y1:y2, x1:x2]
    cv2.imwrite( "/home/ahalyamandana/sign_language_project/tf_files/sign_photos/test.jpg", img_cropped);

        
           
# Following line should appear but is not working with opencv-python package
cap.release()
cv2.destroyAllWindows()
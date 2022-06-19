# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 22:36:21 2022

@author: sdeni
"""
## Shi-Tomasi Corner Detector & Good Features to Track
import cv2 
import numpy as np

img = cv2.imread("./input_images/grains.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y), 3, 255, -1)

cv2.imshow("corners", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
    
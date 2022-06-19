# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 22:02:40 2022

@author: sdeni
"""
##HARRIS
import cv2 
import numpy as np

img = cv2.imread("./input_images/grains.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

harris = cv2.cornerHarris(gray, 2, 3, 0.04)

img[harris> 0.01*harris.max()] = [255, 0, 0]

cv2.imshow("harris", img)

cv2.waitKey(5000)
cv2.destroyAllWindows()
 

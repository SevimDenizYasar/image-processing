# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 21:22:17 2022

@author: sdeni
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("./input_images/BSE_Google_noisy.jpg", 0)


ret, th = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU+ cv2.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8)
erosion = cv2.erode(th, kernel, iterations=1)
dilation = cv2.dilate(erosion, kernel, iterations=1)
opening= cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel) # same results with erosion + dilation 

#plt.hist(img.flat, bins=100, range=(0,255))

cv2.imshow("original", img)
cv2.imshow("OTSU", th)
cv2.imshow("eroded", erosion)
cv2.imshow("dilated", dilation) 
cv2.imshow("opened", opening)

cv2.waitKey(5000)
cv2.destroyAllWindows()



## first denoise by applying median then threshold 

median = cv2.medianBlur(img, 3)
ret, th = cv2.threshold(median, 0, 255, cv2.THRESH_OTSU+ cv2.THRESH_BINARY)

cv2.imshow("median", median)
cv2.imshow("median+threshold", th)

cv2.waitKey(5000)
cv2.destroyAllWindows()







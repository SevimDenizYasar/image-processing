# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 22:42:22 2022

@author: sdeni
"""
## corner detector
import cv2 
import numpy as np

img = cv2.imread("./input_images/grains.jpg", 0)

detector = cv2.FastFeatureDetector_create(50)

kp = detector.detect(img, None)

img2 =cv2.drawKeypoints(img, kp, None, flags=0)

cv2.imshow("corners", img2)
cv2.waitKey(5000)
cv2.destroyAllWindows()
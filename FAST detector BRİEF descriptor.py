# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 22:51:16 2022

@author: sdeni
"""
## FAST detector BRİEF descriptor

import cv2 


img = cv2.imread("./input_images/grains.jpg", 0)

orb = cv2.ORB_create(50)

kp, des = orb.detectAndCompute(img, None)

img2 =cv2.drawKeypoints(img, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("ORB", img2)
cv2.waitKey(5000)
cv2.destroyAllWindows()
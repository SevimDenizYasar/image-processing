# -*- coding: utf-8 -*-
"""
Created on Tue May 24 20:55:28 2022

@author: sdeni
"""

import cv2
import numpy as np

img =cv2.imread("./input_images/lena_noisy.jfif", 0)
canny_edge = cv2.Canny(img, 10, 30)

#♠OR AUTO CANNY

sigma = 0.3
median = np.median(img)

lower = int(max(0,(1.0-sigma)*median))
upper = int(min(255, (1.0 +sigma)*median))

auto_canny = cv2.Canny(img, lower, upper)

cv2.imshow("canny", canny_edge)
cv2.imshow("auto canny", auto_canny) 

cv2.waitKey(5000)
cv2.destroyAllWindows()

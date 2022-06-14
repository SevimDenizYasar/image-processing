# -*- coding: utf-8 -*-
"""
Created on Tue May 24 20:47:12 2022

@author: sdeni
"""

import cv2
from skimage.filters import roberts, sobel, scharr, prewitt

img= cv2.imread("./input_images/lena_color.tiff", 0)
roberts_img = roberts(img)
sobel_img = sobel(img)
scharr_img = scharr(img)
prewitt_img = prewitt(img)

cv2.imshow("roberts", roberts_img)
cv2.imshow("sobel", sobel_img) #best way
cv2.imshow("scharr", scharr_img)
cv2.imshow("prewitt", prewitt_img)

cv2.waitKey(5000)
cv2.destroyAllWindows()
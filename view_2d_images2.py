# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:18:52 2022

@author: sdeni
"""
import cv2 
from skimage import io
img = io.imread("C:/Users/sdeni/OneDrive/Belgeler/software/input_images/lena_color.tiff")



gray_img = cv2.imread("C:/Users/sdeni/OneDrive/Belgeler/software/input_images/lena_color.tiff", 0)
color_img = cv2.imread("C:/Users/sdeni/OneDrive/Belgeler/software/input_images/lena_color.tiff", 1)

img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow ("pic from skimage import", img)
cv2.imshow("color pic from opencv", color_img)
cv2.imshow("gray pic from opencv", gray_img)

cv2.waitKey(2000)
cv2.destroyAllWindows()


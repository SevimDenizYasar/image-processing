# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:58:44 2022

@author: sdeni
"""

from matplotlib import pyplot as plt
import cv2 

gray_img =cv2.imread("C:/Users/sdeni/OneDrive/Belgeler/software/input_images/lena_color.tiff", 0)
plt.imshow(gray_img, cmap= "gray")
plt.hist(gray_img.flat, bins =100, range =(0 ,150))

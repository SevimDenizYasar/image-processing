# -*- coding: utf-8 -*-
"""
Created on Thu May 26 17:23:13 2022

@author: sdeni
"""

import matplotlib.pyplot as plt
from skimage import filters, morphology
import cv2 
import numpy as np


img =cv2.imread("./input_images/scratch1.jpg", cv2.COLOR_BAYER_BGGR2GRAY)
entr_img =filters.rank.entropy(img, morphology.disk(3))
plt.imshow(entr_img, cmap="gray")

thresh = filters.threshold_otsu(entr_img)
binary = entr_img <= thresh

plt.imshow(binary, cmap ='gray')

plt.show(thresh)
print(entr_img.shape)
print("white percentage", (np.sum(binary==1)*100)/(np.sum(binary==0) +np.sum(binary==1)))


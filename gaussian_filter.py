# -*- coding: utf-8 -*-
"""
Created on Tue May 24 20:10:30 2022

@author: sdeni
"""

from skimage import io
import cv2
from skimage.filters import gaussian
from matplotlib import pyplot as plt

img = io.imread("./input_images/microscope3.jpg", as_gray =False)

gaussian_cv2 = cv2.GaussianBlur(img, (3, 3), 0, borderType = cv2.BORDER_CONSTANT)
gaussian_skimage = gaussian(img, sigma = 2, mode='constant', cval= 0.0 )


cv2.imshow("original", img)
cv2.imshow("gaussian cv2", gaussian_cv2)
cv2.imshow("gaussian skimage", gaussian_skimage)

plt.imsave("./input_images/microscope3_blur2.jpg",gaussian_skimage, cmap='gray')

cv2.waitKey(5000)
cv2.destroyAllWindows()

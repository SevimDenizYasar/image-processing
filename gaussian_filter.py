# -*- coding: utf-8 -*-
"""
Created on Tue May 24 20:10:30 2022

@author: sdeni
"""

from skimage import io
import cv2
from skimage.filters import gaussian


img = io.imread("./input_images/lena_image.png", as_gray= True)

gaussian_cv2 = cv2.GaussianBlur(img, (3, 3), 0, borderType = cv2.BORDER_CONSTANT)
gaussian_skimage = gaussian(img, sigma = 4, mode='constant', cval= 0.0 )


cv2.imshow("original", img)
cv2.imshow("gaussian cv2", gaussian_cv2)
cv2.imshow("gaussian skimage", gaussian_skimage)



cv2.waitKey(5000)
cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
"""
Created on Tue May 24 20:30:04 2022

@author: sdeni
"""

from skimage import io
import cv2
from skimage.filters import median
from skimage.morphology import disk


img = io.imread("./input_images/lena_image.png", as_gray= True)

median_cv2 = cv2.medianBlur(img.astype('float32'), 3)
median_skimage = median(img, disk(3), mode = 'constant', cval= 0.0)


cv2.imshow("original", img)
cv2.imshow("median cv2", median_cv2)
cv2.imshow("median skimage", median_skimage)



cv2.waitKey(5000)
cv2.destroyAllWindows()

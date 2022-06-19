# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:09:59 2022

@author: sdeni
"""
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("./input_images/Alloy.jpg", 0)
eq_img = cv2.equalizeHist(img)

#plt.hist(eq_img.flat, bins=100, range=(0,255))

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl_img = clahe.apply(img)

plt.hist(cl_img.flat, bins=100, range=(100,255))

ret, thresh1 = cv2.threshold(cl_img, 190, 150, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(cl_img, 190, 255, cv2.THRESH_BINARY_INV)

ret2, thresh3 =cv2.threshold(cl_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("ORİGİNAL", img)
cv2.imshow("clahe",thresh1)
cv2.imshow("clahe_INV",thresh2)
cv2.imshow("OTSU",thresh3)
cv2.waitKey(5000)
cv2.destroyAllWindows()
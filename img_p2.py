from skimage import io
import cv2
from matplotlib import pyplot as plt
import numpy as np
import tifffile 
import czifile



img = io.imread("C:/Users/sdeni/Downloads/lena_color.tiff" , as_gray = True)

gray_img = cv2.imread("C:/Users/sdeni/Downloads/lena_color.tiff", 0)
color_img = cv2.imread("C:/Users/sdeni/Downloads/lena_color.tiff", 1)
img_tiff = tifffile.imread("C:/Users/sdeni/Downloads/lena_color.tiff")

img_czi= czifile.imread("C:/Users/sdeni/Downloads/CZI_IMAGE_SAMPLE.czi")
print(img_czi.shape)
img1 = img[0, 0, :, :, :, 0]
print(img1.shape)
img2 = img1[0, :, :]
img3 = img1[1, :, :]
img4 = img1[2, :, :]
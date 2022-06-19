# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 16:55:10 2022

@author: sdeni
"""

import cv2
from skimage import img_as_ubyte, img_as_float, io
from skimage.restoration import denoise_nl_means, estimate_sigma
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage as nd

img = img_as_float(cv2.imread("./input_images/BSE_Google_noisy.jpg", cv2.IMREAD_GRAYSCALE))
#print(len(img.shape))
img_float32 = np.float32(img)
multichannel_image = cv2.cvtColor(img_float32, cv2.COLOR_GRAY2BGR)
#print(len(lab_image.shape))
sigma_est =np.mean(estimate_sigma(multichannel_image, multichannel =True))
denoise = denoise_nl_means(multichannel_image, h=1.5 * sigma_est, fast_mode=True,patch_size = 5, patch_distance=3, multichannel =True)
denoise_gray = cv2.cvtColor(denoise, cv2.COLOR_BGR2GRAY)
denoise_ubyte = img_as_ubyte(denoise_gray)

#plt.imshow(denoise, cmap='gray')
#plt.imshow(denoise_ubyte, cmap='gray')
#plt.hist(denoise_ubyte.flat, bins=100, range=(0,80))
segm1 = (denoise_ubyte <= 55)
segm2 = (denoise_ubyte > 55) & (denoise_ubyte <= 110)
segm3 = (denoise_ubyte > 110) & (denoise_ubyte <= 210)
segm4 = (denoise_ubyte > 210)

all_segments = np.zeros((denoise_ubyte.shape[0], denoise_ubyte.shape[1],3))
all_segments[segm1] = (1,0,0)
all_segments[segm2] = (0,1,0)
all_segments[segm3] = (0,0,1)
all_segments[segm4] = (1,1,0)

#plt.imshow(all_segments)

#BINARY CLOSING/OPENING 

segm1_opened = nd.binary_opening(segm1, np.ones((3,3)))
segm1_closed = nd.binary_closing(segm1_opened, np.ones((3,3)))

segm2_opened = nd.binary_opening(segm2, np.ones((3,3)))
segm2_closed = nd.binary_closing(segm2_opened, np.ones((3,3)))


segm3_opened = nd.binary_opening(segm3, np.ones((3,3)))
segm3_closed = nd.binary_closing(segm3_opened, np.ones((3,3)))


segm4_opened = nd.binary_opening(segm4, np.ones((3,3)))
segm4_closed = nd.binary_closing(segm4_opened, np.ones((3,3)))

all_segments_cleaned = np.zeros((denoise_ubyte.shape[0], denoise_ubyte.shape[1],3))

all_segments_cleaned[segm1_closed] = (1,0,0)
all_segments_cleaned[segm2_closed] = (0,1,0)
all_segments_cleaned[segm3_closed] = (0,0,1)
all_segments_cleaned[segm4_closed] = (1,1,0)



plt.imsave("./output_images/segmented.jpg",all_segments_cleaned)




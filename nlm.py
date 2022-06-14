# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:57:38 2022

@author: sdeni
"""

from skimage import io, img_as_float
from skimage.restoration import denoise_nl_means, estimate_sigma
from scipy import ndimage as nd
from matplotlib import pyplot as plt
import numpy as np
import cv2

img=img_as_float(io.imread("./input_images/noisy_img.jpg"))

gaussian_img=nd.gaussian_filter(img, 3)

median_img=nd.median_filter(img,size=3)
sigma_est = np.mean(estimate_sigma(img, multichannel=True))
nlm2_img = denoise_nl_means(img,h =1.5*sigma_est, fast_mode=True, patch_size=5, patch_distance=3, multichannel=True )

plt.imsave("./output_images/nlm2_img.jpg", nlm2_img)
#plt.imsave("./output_images/median_noisy.jpg", median_img)




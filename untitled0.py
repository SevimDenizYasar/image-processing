# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:51:33 2022

@author: sdeni
"""

from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_float, img_as_ubyte, io
import numpy as np
from matplotlib import pyplot as plt
import cv2

#img =img_as_float(cv2.imread("./input_images/BSE_Google_noisy.jpg", cv2.COLOR_BAYER_BG2RGB))
img = img_as_float(io.imread("./input_images/BSE_Google_noisy.jpg"))

sigma_est = np.mean(estimate_sigma(img, multichannel=True))
denoised = denoise_nl_means(img, h= 1.5* sigma_est, fast_mode=False, patch_size=5, patch_distance= 3, multichannel=True)
plt.imshow(denoised, cmap= "gray")
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 23:03:20 2022

@author: sdeni
"""

from skimage import io, img_as_float, exposure, color
import matplotlib.pyplot as plt
import numpy as np
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage.segmentation import random_walker
import cv2

img = img_as_float(io.imread("./input_images/Alloy_noisy.jpg"))

#plt.hist(img.flat, bins=100, range=(0,1))

sigma_est =np.mean(estimate_sigma(img, multichannel =True))

patch_kw = dict(patch_size=5,
                patch_distance=6,
                multichannel=True)
img_float32 = np.float32(img)

multichannel_image = cv2.cvtColor(img_float32, cv2.COLOR_GRAY2BGR)
denoise_img = denoise_nl_means(multichannel_image, h=1.15 * sigma_est, fast_mode=True,**patch_kw)
denoise_gray = cv2.cvtColor(denoise_img, cv2.COLOR_BGR2GRAY)
eq_img = exposure.equalize_adapthist(denoise_img)


#plt.imshow(eq_img, cmap="gray")
#plt.hist(eq_img.flat, bins=100, range=(0,1))
print(multichannel_image.shape)
markers = np.zeros(multichannel_image.shape, dtype=np.uint)
markers[(eq_img < 0.6)]=1
markers[(eq_img > 0.6)]=2

#plt.imshow(markers)

labels=random_walker(eq_img, markers, beta=10, mode='bf')
                      
plt.imshow(labels)













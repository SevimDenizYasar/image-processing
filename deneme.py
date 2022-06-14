# -*- coding: utf-8 -*-
"""
Created on Tue May 24 19:34:37 2022

@author: sdeni
"""

from matplotlib import pyplot as plt
from skimage import io, color
from skimage.transform import rescale, resize, downscale_local_mean

img = io.imread("C:/Users/sdeni/OneDrive/Belgeler/software/input_images/lena_color2.jpg", 0)


img_rescaled = rescale(img, 1.0/4.0)

plt.imshow(img)
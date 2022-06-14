# -*- coding: utf-8 -*-
"""
Created on Tue May 24 19:02:07 2022

@author: sdeni
"""
from matplotlib import pyplot as plt
from skimage import io, color
#from skimage.transform import rescale, resize, downscale_local_mean

img = io.imread("C:/Users/sdeni/OneDrive/Belgeler/software/input_images/lena_color.tiff")
plt.imshow(img)

#+img_rescaled = rescale(img, 1.0/4.0 , anti_aliasing=False)
#img_resized = resize(img, (200, 200) , anti_aliasing=True)
#plt.imshow(img_rescaled)


#img_downscaled =downscale_local_mean(img, (4,3))


from skimage.filters import gaussian, sobel

gaussian_img_sk= gaussian(img, sigma =4, mode = 'constant', cval=0.0)
plt.imshow(gaussian_img_sk)

img_gray = io.imread("C:/Users/sdeni/OneDrive/Belgeler/software/input_images/lena_image.png", 1)

#sobel_img = sobel(img_gray )
plt.imshow(img_gray)
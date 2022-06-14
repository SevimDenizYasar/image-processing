from skimage import io, img_as_ubyte
img = io.imread("C:/Users/sdeni/OneDrive/Belgeler/software/input_images/lena_color.tiff")

from skimage import filters
gaussian_img = filters.gaussian(img, sigma=3)
# io.imsave("C:/Users/sdeni/Downloads/saved2_using_skimage.jpg", gaussian_img)
# io.imsave("C:/Users/sdeni/Downloads/color_lena.jpg", img)
gaussian_img_8bit= img_as_ubyte(gaussian_img)
io.imsave("C:/Users/sdeni/OneDrive/Belgeler/software/output_images/ubyte_gaussian.jpg", gaussian_img_8bit)


import cv2 

cv2.imwrite("C:/Users/sdeni/OneDrive/Belgeler/software/output_images/saved_using_opencv.jpg",gaussian_img_8bit )
gaussian_img_8bit = cv2.cvtColor(gaussian_img_8bit, cv2.COLOR_BGR2RGB)
cv2.imwrite("C:/Users/sdeni/OneDrive/Belgeler/software/output_images/BRG2RGB_saved_using_opencv.jpg",gaussian_img_8bit )

from matplotlib import pyplot as plt
plt.imsave("C:/Users/sdeni//OneDrive/Belgeler/software/output_images/saved_using_pyplot.jpg", gaussian_img)

import tifffile
tifffile.imwrite("C:/Users/sdeni/OneDrive/Belgeler/software/output_images/saved_using_tiffile.tiff", gaussian_img_8bit)
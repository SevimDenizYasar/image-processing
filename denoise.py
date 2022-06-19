import cv2
from skimage import img_as_ubyte, img_as_float, io
from skimage.restoration import denoise_nl_means, estimate_sigma
import numpy as np
from matplotlib import pyplot as plt

img = img_as_float(io.imread("./input_images/BSE_Google_noisy.jpg"))
#print(len(img.shape))
img_float32 = np.float32(img)
multichannel_image = cv2.cvtColor(img_float32, cv2.COLOR_GRAY2BGR)
#print(len(lab_image.shape))
sigma_est =np.mean(estimate_sigma(multichannel_image, multichannel =False))
denoise = denoise_nl_means(multichannel_image, h=1.5 * sigma_est, fast_mode=True,patch_size = 5, patch_distance=3, multichannel =True)
plt.imshow(denoise, cmap='gray')
plt.show()

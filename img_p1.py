from skimage import io, img_as_float, img_as_ubyte
import cv2

img = io.imread("C:/Users/sdeni/Downloads/lena_color.tiff")
print(img.shape)

img2 = img_as_float(img)
img3 = img_as_ubyte(img2)

img_cv2 = cv2.imread("C:/Users/sdeni/Downloads/lena_color.tiff")
img_cv2_color = cv2.imread("C:/Users/sdeni/Downloads/lena_color.tiff", 1)

img_opencv = cv2.cvtColor(img_cv2_color, cv2.COLOR_BGR2RGB)





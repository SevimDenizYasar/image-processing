from skimage import io, filters
from matplotlib import pyplot as plt

img = io.imread("C:/Users/sdeni/OneDrive/Belgeler/software/input_images/lena_color.tiff")

io.imshow(img)



img_gray =io.imread("C:/Users/sdeni/OneDrive/Belgeler/software/input_images/lena_color.tiff", as_gray =True)
#plt.imshow(img_gray, cmap ="hot")
#plt.imshow(img_gray, cmap ="jet")


fig = plt.figure(figsize=(10,10))

ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img_gray, cmap="hot")
ax1.title.set_text("1st")

ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img_gray, cmap="jet")
ax2.title.set_text("2nd")

ax3 = fig.add_subplot(2,2,3)
ax3.imshow(img_gray, cmap="gray")
ax3.title.set_text("3rd")

ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img_gray, cmap="nipy_specural")
ax4.title.set_text("4th")
plt.show()
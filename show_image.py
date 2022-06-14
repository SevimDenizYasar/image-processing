from skimage import io
import sys

def save(image):
  io.imsave("C:/Users/sdeni/OneDrive/Belgeler/software/output_images/test.jpg", image)

sys.modules[__name__] = save
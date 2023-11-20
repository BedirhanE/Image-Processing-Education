from PIL import Image, ImageOps  # I installed the python pillow package.

resim='bedirhan.jpg'

#I used the open() function to open the file
Image.open(resim).show()
im = ImageOps.grayscale(Image.open(resim))
im.save("gray.jpg")
im.show("gray.jpg")

#orjinal image i gray şekilde ekrana getirmiş oldum
im = Image.open(resim)
im.rotate(45).save("rotate.jpg")  #45 degree rotation operation 
im.show("rotate.jpg")

import cv2
import matplotlib.pyplot as plt

imgpath = "gray.jpg"
img = cv2.imread(imgpath,0)


plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.title('image')
plt.xticks([])
plt.yticks([])

plt.subplot(1,2,2)
plt.hist(img.ravel(),256,[0,255],color="pink")
plt.title('histogram')

plt.show()

#I have blurred the original image.
from PIL import Image, ImageFilter
im = Image.open(resim)
im.filter(ImageFilter.BLUR).show()
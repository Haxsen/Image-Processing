import numpy as np
import cv2 as cv
import math
from matplotlib import pyplot as plt

img = np.array(cv.imread('coin.jpg', 0))
size = np.shape(img)

imgx = cv.imread('coin.jpg',0)
edges = cv.Canny(img,100,200)

plt.subplot(121),plt.imshow(imgx,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Canny Edged'), plt.xticks([]), plt.yticks([])

plt.show()
import numpy as np
import cv2 as cv
import math
from matplotlib import pyplot as plt

img = np.array(cv.imread('coin.jpg', 0))
size = np.shape(img)

#Task1
buff1 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])  #vertical
buff2 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  #horizontal
img1 = cv.filter2D(img, -1, buff1)  #applying vertical buffer
img2 = cv.filter2D(img, -1, buff2)  #applying horizontal buffer
#write files
cv.imwrite('verticalsobel.jpg', img1)
cv.imwrite('horizontalsobel.jpg', img2)
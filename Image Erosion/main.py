import cv2 as cv
import numpy as np

def ErodePixel(x,y, image,size):
    out=255

    if x!=0 & y!=0:
        if image[x-1,y-1]!=255:
            out=0
    if x!=0:
        if y!=0:
            if image[x-1,y-1]!=255:
             out=0
        if image[x-1, y]!=255:
            out=0
        if image[x-1, y+1]!=255:
            out=0
    if y!=0:
        if x!=0:
            if image[x-1, y-1]!=255:
               out=0
        if image[x, y-1]!=255:
            out=0
        if image[x+1, y-1]!=255:
            out=0
    if x!=(size[0]-1):
        if image[x+1,y-1]!=255:
            out=0
        if image[x+1, y]!=255:
            out=0
        if image[x+1, y+1]!=255:
            out=0
    if y!=(size[1]-1):
        if image[x-1, y+1]!=255:
            out=0
        if image[x, y+1]!=255:
            out=0
        if image[x+1, y+1]!=255:
            out=0
    if x!=(size[0]-1) & y!=(size[1]-1):
        if image[x+1,y+1]!=255:
            out=0

    return out

def DilatePixel(x,y, image,size):
    out=255

    return out

def ErodeImage(image,size):
    for i in range(size[0]):
        for j in range(size[1]):
            if image[i,j] !=0:
                image[i,j]=ErodePixel(i,j,image,size)
    return image
def DilateImage(image,size):
    for i in range(size[0]):
        for j in range(size[1]):
            if image[i,j] !=0:
                image[i,j]=DilatePixel(i,j,image,size)
    return image

#task 1
img = cv.imread('fig1.jpg', 0)
cv.imshow('original 1',img)
sz = np.shape(img)
#eimg1x = ErodeImage(img,sz)
eimg1 = cv.erode(img, np.ones((2,2),np.uint8), iterations=16)
cv.imshow('eroded 1',eimg1)

#task 2
img2 = cv.imread('fig2.jpg', 0)
cv.imshow('original 2',img2)
sz2 = np.shape(img2)
#dimg2x = DilateImage(img2,sz2)
dimg2 = cv.erode(img2, np.ones((2,2),np.uint8), iterations=2)
dimg2 = cv.dilate(dimg2, np.ones((2,2),np.uint8), iterations=1)
cv.imshow('eroded and dilated 2',dimg2)

#task 3
img3 = cv.imread('fig3.jpg', 0)
cv.imshow('original 3',img3)
sz3 = np.shape(img3)
pimg3 = cv.dilate(img3, np.ones((3,3),np.uint8), iterations=1)
pimg3 = cv.erode(pimg3, np.ones((3,3),np.uint8), iterations=1)
kernel = np.ones((5,5),np.uint8)
gradient = cv.morphologyEx(pimg3, cv.MORPH_GRADIENT, kernel)
cv.imshow('Eroded, Dilated and Morph Gradiented',gradient)

cv.waitKey()
import cv2
import numpy as np

def get8n(x, y, shape):
    out = []
    maxx = shape[1]-1
    maxy = shape[0]-1

    #top left
    outx = min(max(x-1,0),maxx)
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #top center
    outx = x
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #top right
    outx = min(max(x+1,0),maxx)
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #left
    outx = min(max(x-1,0),maxx)
    outy = y
    out.append((outx,outy))

    #right
    outx = min(max(x+1,0),maxx)
    outy = y
    out.append((outx,outy))

    #bottom left
    outx = min(max(x-1,0),maxx)
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    #bottom center
    outx = x
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    #bottom right
    outx = min(max(x+1,0),maxx)
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    return out

def region_growing(img, seed):
    list = []
    outimg = np.zeros_like(img)
    list.append((seed[0], seed[1]))
    processed = []
    while(len(list) > 0):
        pix = list[0]
        outimg[int(pix[0]), int(pix[1])] = 255
        for coord in get8n(pix[0], pix[1], img.shape):
            if img[int(coord[0]), int(coord[1])] != 0:
                outimg[int(coord[0]), int(coord[1])] = 255
                if not coord in processed:
                    list.append(coord)
                processed.append(coord)
        list.pop(0)
        cv2.imshow("progress",outimg)
        cv2.waitKey(1)
    return outimg


image = cv2.imread('circle.jpg', 0)
mysize=np.shape(image)
clicks=[]
clicks.append(((mysize[0])/2, (mysize[1])/2))
print(clicks)
ret, img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
cv2.namedWindow('Input')
cv2.imshow('Input', img)
cv2.waitKey()
seed = clicks[-1]
out = region_growing(img, seed)
cv2.imshow('Region Growing', out)
cv2.waitKey()
cv2.destroyAllWindows()
import cv2
import random
import numpy as np

def sp_noise(image,prob):
    output=np.zeros(image.shape,np.uint8)
    thres=1-prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn=random.random()
            if rdn<prob:
                output[i][j]=0
            elif rdn>thres:
                output[i][j]=255
            else:
                output[i][j]=image[i][j]
    return output

img=cv2.imread("C:/Users/User/1053/car.jpg")
lGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

noisyImg=sp_noise(lGray,0.05)

cv2.imshow('Input image',img)
cv2.imshow('Noisy image',noisyImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
    

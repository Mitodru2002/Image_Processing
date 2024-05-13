import math
import numpy as np
import cv2

gray = cv2.imread("D:/user/car.JPG",0)
h, w = gray.shape
gamma=np.zeros([h,w],dtype=np.uint8)

for i in range(h):
    for j in range(w):
        gamma[i, j] = 95*math.pow(gray[i,j],.3)

cv2.imshow('gray', gray)
cv2.imshow('gamma', gamma)

cv2.waitKey(0)
cv2.destroyAllWindows()

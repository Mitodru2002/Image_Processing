import math
import numpy as np
import cv2

gray = cv2.imread("D:/User/car.JPG",0)
h, w = gray.shape
first=np.zeros([h,w],dtype=np.uint8)
second=np.zeros([h, w], dtype=np.uint8)
third=np.zeros([h,w],dtype=np.uint8)

for i in range(h):
    for j in range(w):
        first[i, j] = 50*math.log(gray[i,j]+1)
        second[i,j]=100*math.log(gray[i,j]+1)
        third[i,j]=150*math.log(gray[i,j]+1)

cv2.imshow('gray', gray)
cv2.imshow('first', first)
cv2.imshow('second', second)
cv2.imshow('third', third)



cv2.waitKey(0)
cv2.destroyAllWindows()

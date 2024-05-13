import matplotlib.pyplot as plt
import numpy as np
import cv2

img=cv2.imread("C:/Users/car.jpg")
h,w,c=img.shape

R=np.zeros([h,w],dtype=np.uint8)
G=np.zeros([h,w],dtype=np.uint8)
B=np.zeros([h,w],dtype=np.uint8)

for i in range(h):
    for j in range(w):
        B[i,j]=img[i,j,0]
        G[i,j]=img[i,j,1]
        R[i,j]=img[i,j,2]

Red=cv2.imshow("Red",R)
Green=cv2.imshow("Green",G)
Blue=cv2.imshow("Blue",B)


cv2.imshow("marge",cv2.marge([R,G,B]))


cv2.waitKey(0)
cv2.destroyAllWindows()

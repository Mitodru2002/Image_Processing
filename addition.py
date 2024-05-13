import cv2
import numpy as np
import matplotlib.pyplot as plt   
img1=cv2.imread('D:/1053/image/456.jpg')
img2=cv2.imread('D:/1053/image/444.jpg')
grey1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
grey2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('grey1',grey1)
cv2.imshow('grey2',grey2)
H,W,D=img1.shape
h,w,d=img2.shape
new=np.zeros([H,W],dtype=np.uint8)
for i in range(H):
      for j in range(W):
          new[i,j]=int((grey1[i,j]+grey2[i,j]))
cv2.imshow('new',new)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
def split(img):
    B,G,R=cv2.split(img)
    H,W,D=img.shape
    blank=np.zeros([H,W],dtype=np.uint8)
    blue = cv2.merge ([B,blank,blank])
    green = cv2.merge ([blank,G,blank])
    red = cv2.merge ([blank,blank,R])
    cv2.imshow('blue',blue)
    cv2.imshow('red',red)
    cv2.imshow('green',green)
    cv2.imshow('img',img)
    
img=cv2.imread('D:/1053/image/img3.jpg')
split(img)
cv2.waitKey(0)
cv2.destroyAllWindows()

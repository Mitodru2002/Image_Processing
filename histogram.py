import cv2
import numpy as np
import matplotlib.pyplot as plt
def gray_conversion(img):
    H,W,D=img.shape
    B,G,R=cv2.split(img)
    gray=np.zeros([H,W],dtype=np.uint8)
    for i in range(H):
        for j in range(W):
            gray[i,j]=int((B[i,j] + G[i,j] +R[i,j])/3.0)
    cv2.imshow('gray',gray)
    return gray

def histogram(img):
    gray=gray_conversion(img)
    H,W,D=img.shape
    histo=np.zeros([256],dtype=np.uint8)
    for i in range(H):
      for j in range(W):
          intensity = gray[i,j]
          histo[intensity]+=1
    plt.bar(np.arange(len(histo)),histo)
    plt.show()
    
    print(histo)
    



   
      
    

img=cv2.imread('D:/1053/image/kk.jpg')
histogram(img)
cv2.waitKey(0)
cv2.destroyAllWindows()








import numpy as np
import cv2
import matplotlib.pyplot as plt

gray=cv2.imread("C:/Users/car.jpg")
h,w=gray.shape

def histogram(img):
    h,w = img.shape
    hist=np.zeros(256,dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            ind=img[i,j]
            hist[ind]=hist[ind]+1
    return hist

def gray_slicing(img):
    h,w=img.shape
    g_l_sliced=np.zeros([h,w],dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if img[i,j]>=100 and img[i,j]<=200:
                g_l_sliced[i,j]=255
            else:
                g_l_sliced[i,j]=img[i,j]
    return g_l_sliced

g_l_sliced=gray_slicing(gray)
cv2.imshow("gray level sliced",g_l_sliced)
hist_img=histogram(gray)
plt.gray(np.arange(len(hist_img)),hist_img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

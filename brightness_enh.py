import matplotlib.pyplot as plt
import numpy as np
import cv2

img=cv2.imread("C:/Users/User/1053/car.jpg")

def grayConversion(img):
    h, w, c = img.shape
    R, G, B = cv2.split(img)
    gray = np.zeros([h, w], dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            gray[i, j] = int(R[i, j] * 0.114 + G[i, j] * 0.587 + B[i, j] * 0.299)
    return gray
def contrast_stretching(img):
    h,w=img.shape
    min= np.min(img)
    max= np.max(img)
    stretched_img=(img-min)*(255/(max-min))
    return stretched_img.astype(np.uint8)
def histogram(img):
    h, w = img.shape
    hist=np.zeros([256],dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            ind=img[i,j]
            hist[ind]=hist[ind]+1
    return hist
def brightness_increase(img)
    h, w = img.shape
    min = np.min(img)
    max = np.max(img)
    s=int(input("Enter the starting value"))
    e=int(input("Enter the starting value"))
    bright_img=np.zeros([h,w],dtype=uint8)
    for i in range(h)
        for j in range(w)
            bright_img[i,j]=(gray[i,j]-min)/((max-min)*(s-e)+s)
    return bright_img
#brightness
bright_img=brightness_increase(grayImg)
hist_img3=histogram(bright_img)
plt.bar(np.arange(len(img2)),img2)
#histogram grayimage
grayImg=grayConversion(img)
hist=histogram(grayImg)
plt.bar(np.arange(len(hist)),hist)
img1=cv2.imshow("gray image",grayImg)
plt.show()

#histogram contrastimage
str_img=contrast_stretching(grayImg)
img2=cv2.imshow("stretched image",str_img)
hist2=histogram(str_img)
plt.bar(np.arange(len(hist2)),hist2)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

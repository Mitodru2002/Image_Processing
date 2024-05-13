import matplotlib.pyplot as plt
import numpy as np
import cv2

gray = cv2.imread("C:/Users/car.jpg",0)
h, w = gray.shape

neg = np.zeros([h, w], dtype=np.uint8)
for i in range(h):
    for j in range(w):
        neg[i, j] = 255 - gray[i, j]

cv2.imshow('Negative', neg)
cv2.waitKey(0)
cv2.destroyAllWindows()

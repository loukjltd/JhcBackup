import numpy as np
import cv2

wImg = cv2.imread('white_pic.png', 0)
h, w = wImg.shape[0:2]
cv2.imshow('Original White Img', wImg)

binary = np.zeros([h, w, 1], 'uint8')

thresh = 85

for r in range(0, h):
    for c in range(0, w):
        if wImg[r][c] > thresh:
            binary[r][c] = 255

cv2.imshow('Slow Binary', binary)

r, t = cv2.threshold(wImg, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow('CV Threshold', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

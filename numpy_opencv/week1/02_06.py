import numpy as np
import cv2

img = cv2.imread('thresh.jpg')
cv2.imshow('Original', img)

blurImg = cv2.GaussianBlur(img, (5, 55), 0)
cv2.imshow('Original', blurImg)

kernel = np.ones((5, 5), 'uint8')

dilate = cv2.dilate(img, kernel, iterations=1)
erode = cv2.erode(img, kernel, iterations=1)

cv2.imshow('Dilate', dilate)
cv2.imshow('Erode', erode)

cv2.waitKey(0)
cv2.destroyAllWindows()

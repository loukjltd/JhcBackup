import numpy as np
import cv2

img = cv2.imread('sudo.png', 0)
cv2.imshow('Original', img)

r, t_b = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
cv2.imshow('Basic Binary', t_b)

t_a = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('Adaptive Threshold', t_a)

cv2.waitKey(0)
cv2.destroyAllWindows()
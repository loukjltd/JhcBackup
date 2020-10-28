import numpy as np
import cv2

img = cv2.imread('players.jpg', 1)

# Scale the Img to Half
img_half = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('Half Img', img_half)

# Scale the Img to Double
img_double = cv2.resize(img, (0, 0), fx=2, fy=2)
cv2.imshow('Double Img', img_double)

# Rotate the Img 45 Degrees
M = cv2.getRotationMatrix2D((0, 0), -45, 1)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow('Rotated Img 45', rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()

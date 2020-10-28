import numpy as np
import cv2

black = np.zeros([150, 200, 1], 'uint8')
cv2.imshow('BlackImg', black)
print(black[0, 0, :])

ones = np.ones([150, 200, 2], 'uint8')
cv2.imshow('OnesImg', ones)
print(ones[0, 0, :])

white = np.white([150, 200, 3], 'uint16')
white = white * (2 ** 16 - 1)
cv2.imshow('WhiteImg', white)
print(white[0, 0, :])

color = ones.copy()
color[:, :] = (255, 0, 0)
cv2.imshow('BlueImg', color)
print(color[0, 0, :])

cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2

clr = cv2.imread('butterfly.jpg', 1)
cv2.imshow('Img', clr)
cv2.moveWindow('Img', 0, 0)
print(clr.shape)
height, width, channels = clr.shape

b, g, r = cv2.split(clr)

rgb_split = np.empty([height, width * 3, 3], 'uint8')

rgb_split[:, 0: width] = cv2.merge([b, b, b])
rgb_split[:, width:width * 2] = cv2.merge([g, g, g])
rgb_split[:, width * 2:width * 3] = cv2.merge([r, r, r])

cv2.imshow('Channels', rgb_split)
cv2.moveWindow('Channels', 0, height)

hsv = cv2.cvtColor(clr, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
hsv_split = np.concatenate((h, s, v), axis=1)
cv2.imshow('Split HSV', hsv_split)

cv2.waitKey()
cv2.destroyAllWindows()

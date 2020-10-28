import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('video', frame)
    ch = cv2.waitKey(1)
    if ch == 13:
        break

cap.release()
cv2.destroyAllWindows()
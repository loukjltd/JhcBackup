import numpy as np
import cv2

# Global Variables
canvas = np.ones([500, 500, 3], 'uint8') * 255
radius = 10
color = (255, 0, 0)
pressed = False


# Click Callback
def click(event, x, y, flags, param):
    global canvas, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        pressed = True
        cv2.circle(canvas, (x, y), radius, color, -1)
    elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
        cv2.circle(canvas, (x, y), radius, color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        pressed = False


# Windows Initialization and Callback Assigment
cv2.namedWindow('canvas')
cv2.setMouseCallback('canvas', click)

# Forever Draw Loop
while True:
    cv2.imshow('canvas', canvas)

    # Key Capture Every 1ms
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    elif ch & 0xFF == ord('b'):
        color = (255, 0, 0)
    elif ch & 0xFF == ord('g'):
        color = (0, 255, 0)
    elif ch & 0xFF == ord('r'):
        color = (0, 0, 255)

# Destroy All Windows
cv2.destroyAllWindows()

import cv2 as cv
import numpy as np
import sys
from matplotlib import pyplot as plt

#Below is the exmple code from the opencv docs to capture video from webcam and display it in a window. Press 'q' to quit the window.
#Set the argument of cv.VideoCapture() to 0 to use the default webcam, or 1 to use an external webcam. (For this projcet, we will need to use OBS to create a virtual webcam))
cap = cv.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    sys.exit() 

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


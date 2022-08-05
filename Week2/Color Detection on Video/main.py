import cv2 as cv
import numpy as np

def Nothing(i):
    pass

camera = cv.VideoCapture(0)

cv.namedWindow("Frame", cv.WINDOW_NORMAL)

cv.createTrackbar("H1", "Frame", 0, 359, Nothing)
cv.createTrackbar("S1", "Frame", 0, 255, Nothing)
cv.createTrackbar("V1", "Frame", 0, 255, Nothing)
cv.createTrackbar("H2", "Frame", 0, 359, Nothing)
cv.createTrackbar("S2", "Frame", 0, 255, Nothing)
cv.createTrackbar("V2", "Frame", 0, 255, Nothing)

while camera.isOpened():
    
    _, frame = camera.read()
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    H1 = int(cv.getTrackbarPos("H1", "Frame") / 2)
    S1 = cv.getTrackbarPos("S1", "Frame")
    V1 = cv.getTrackbarPos("V1", "Frame")
    H2 = int(cv.getTrackbarPos("H2", "Frame") / 2)
    S2 = cv.getTrackbarPos("S2", "Frame")
    V2 = cv.getTrackbarPos("V2", "Frame")
    
    lower = np.array([H1, S1, V1])
    upper = np.array([H2, S2, V2])
    
    mask = cv.inRange(hsv, lower, upper)
    
    target = cv.bitwise_and(frame, frame, mask = mask)
    
    cv.imshow("Frame", frame)
    cv.imshow("HSV Frame", target)
    
    if cv.waitKey(1) == 27:
        break

camera.release()
cv.destroyAllWindows()
import cv2 as cv

image = cv.imread("Iphone.jpg")
cv.waitKey(0)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

edged = cv.Canny(gray, 30, 200)
cv.waitKey(0)

contours, hierarchy = cv.findContours(edged, 
                                      cv.RETR_EXTERNAL, 
                                      cv.CHAIN_APPROX_NONE)

cv.drawContours(image, contours, -1, (0, 0, 255), 7)
  
cv.imshow('Contours', image)
cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv

image = cv.imread("ellipse.png")
cv.waitKey(0)

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

edged = cv.Canny(gray, 30, 200)
cv.waitKey(0)

contours, hierarchy = cv.findContours(edged, 
                                      cv.RETR_EXTERNAL, 
                                      cv.CHAIN_APPROX_NONE)
""" Multiple Shape/Objects (ellipse.png)
for count, contour in enumerate(contours):
    x,y,w,h= cv.boundingRect(contour)
    croped_image = image[y:(y+h), x:(x+w)]
    cv.imwrite(f'Ellipse {count + 1}.jpg', croped_image)
    cv.waitKey(0)
"""
    
cv.drawContours(image, contours, -1, (0, 0, 255), 7)
  
cv.imshow('Contours', image)
cv.waitKey(0)
cv.destroyAllWindows()
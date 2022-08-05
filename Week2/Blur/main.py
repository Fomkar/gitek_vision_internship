import os
import cv2 as cv
import numpy as np

#%% Compare Blur Types.

# Find Image Path
file = os.getcwd() + "\Media\Rocket.jpg"

# Read Image.
image = cv.imread(file)
image = cv.resize(image, (850, 1440))

# Create 3 Window to Display Blur Types.
cv.namedWindow("Blur", cv.WINDOW_AUTOSIZE)
cv.moveWindow("Blur", 0, 0)

cv.namedWindow("Median Blur", cv.WINDOW_AUTOSIZE)
cv.moveWindow("Median Blur", 850, 0)

cv.namedWindow("Gaussian Blur", cv.WINDOW_AUTOSIZE)
cv.moveWindow("Gaussian Blur", 1700, 0)

# Blur the Image
blur = cv.blur(image, (15, 15))
median_blur = cv.medianBlur(image, 15)
gaussian_blur = cv.GaussianBlur(image, (15,15), 0)

# Open Images in Related Windows.
cv.imshow("Blur", blur)
cv.imshow("Median Blur", median_blur)
cv.imshow("Gaussian Blur", gaussian_blur)

cv.waitKey()
cv.destroyAllWindows()

#%% Sharped Filter

kernel = np.array([[-1,-1,-1], 
                   [-1, 9,-1],
                   [-1,-1,-1]])


sharpened = cv.filter2D(image, -1, kernel) # applying the sharpening kernel to the input image & displaying it.
cv.imshow('Image Sharpening', sharpened)
cv.waitKey(0)
cv.destroyAllWindows()

#%% Erosion and Dilation *** YILDIZ ile yapılacak

rocket = cv.imread("Media\Rocket.jpg", 0)
kernel = np.ones((5, 5), np.uint8)
img_erosion = cv.erode(rocket, kernel, iterations=1)
img_dilation = cv.dilate(rocket, kernel, iterations=1)
 
cv.imshow('Input', rocket)
cv.imshow('Erosion', img_erosion)
cv.imshow('Dilation', img_dilation)
 
cv.waitKey(0)
cv.destroyAllWindows()
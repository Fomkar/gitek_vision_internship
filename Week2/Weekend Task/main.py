import cv2 as cv
from CoordinateFinder import coordinate_finder

#%% Kiwi Detection
kiwi = cv.imread("Media/Kiwi.jpg")

x1, x2, y1, y2 = coordinate_finder(kiwi, 120, 180, "Green")

kiwi_roi = kiwi[y1:y2, x1:x2]
kiwi_gray = cv.cvtColor(kiwi_roi, cv.COLOR_BGR2GRAY)

_, kiwi_threshold = cv.threshold(kiwi_gray, 200, 255, cv.THRESH_BINARY_INV) 

cv.imshow("Kiwi", kiwi_threshold)
cv.imwrite("Media/Kiwi_Threshold.jpg", kiwi_threshold)

cv.waitKey(0)
cv.destroyAllWindows()

#%% Lemon Detection
lemon = cv.imread("Media/Lemon.jpg")

x1, x2, y1, y2 = coordinate_finder(lemon, 180, 255, "Red")

lemon_roi = lemon[y1:y2, x1:x2]
lemon_gray = cv.cvtColor(lemon_roi, cv.COLOR_BGR2GRAY)

_, lemon_threshold = cv.threshold(lemon_gray, 185, 255, cv.THRESH_BINARY)

cv.imshow("Lemon", lemon_threshold)
cv.imwrite("Media/Lemon_Threshold.jpg", lemon_threshold)

cv.waitKey(0)
cv.destroyAllWindows()
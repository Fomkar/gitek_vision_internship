"""
Python Version: 3.8.8
IDE: Spyder 5.0.3
"""

import cv2 as cv

# Create an Empty Function to Callback.
def Nothing(i):
    pass

# Take Image File Name as Input.
image_name = input("Image: ")

# Create an Empty Image.
image = cv.imread(image_name)

# Create a Empty Window to Put Image In.
cv.namedWindow("Image", cv.WINDOW_NORMAL)

# Create Trackbar for RGB Color Values.
cv.createTrackbar("R", "Image", 0, 255, Nothing)
cv.createTrackbar("G", "Image", 0, 255, Nothing)
cv.createTrackbar("B", "Image", 0, 255, Nothing)

# Arrange Base Coloring According to Image File Name.
base_color = (0, 0, 0)

if image_name == "Yellow.jpg":
    base_color = (22, 93, 0)
elif image_name == "Red.jpg":
    base_color = (0, 0, 50)

while True:
    # Put the Image to Empty Window.
    cv.imshow("Image", image)
    
    # Exit the Program When Pressed ESC.
    if cv.waitKey(1) & 0xFF == 27:
        break
    
    # Read RGB Color Values from Trackbar.
    red = cv.getTrackbarPos("R", "Image")
    green = cv.getTrackbarPos("G", "Image")
    blue = cv.getTrackbarPos("B", "Image")
    
    # Arrange Color Masking Values.
    created_color = (red, green, blue)
    
    # Create a Mask.
    mask = cv.inRange(image, base_color, created_color)
    
    # Extract Colored Object from Original Image with Using Mask.
    target = cv.bitwise_and(image, image, mask=mask)
    
    # Show the Masked Image.
    cv.imshow('Mask Color', target)
    
# Close All Windows.
cv.destroyAllWindows()
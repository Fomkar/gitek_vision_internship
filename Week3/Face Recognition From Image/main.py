import os
import cv2 as cv

faceCascade = cv.CascadeClassifier("face_recognition.xml")
suffixes = (".jpg", ".png", ".jpeg")

for file in os.listdir("Media"):
    if file.endswith(suffixes):
        image = cv.imread(f"Media/{file}")
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale(gray, 
                                             scaleFactor = 1.1, 
                                             minNeighbors = 5, 
                                             minSize = (30,30), 
                                             flags = cv.CASCADE_SCALE_IMAGE)
        
        print(f"{file} contains {len(faces)} face(s)!")
        
        for (x, y, w, h) in faces:
            cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv.imshow("Face Recognition", image)
        cv.waitKey(3000)
cv.destroyAllWindows()
import cv2 as cv

faceCascade = cv.CascadeClassifier("face_recognition.xml")

cam = cv.VideoCapture(0)

while cam.isOpened():
    
    ret, frame = cam.read()
    
    if not ret:
        print("Image can't take from Camera.")
        break
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv.CASCADE_SCALE_IMAGE
    )
    
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    cv.imshow("Screen", frame)
    
    if cv.waitKey(1) & 0xFF == 27:
        print("Video Recorded...")
        break
    
cam.release()
cv.destroyAllWindows()
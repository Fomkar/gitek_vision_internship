import cv2 as cv

faceCascade = cv.CascadeClassifier("face_recognition.xml")

cam = cv.VideoCapture(0)

fourCC = cv.VideoWriter_fourcc(*"XVID")

out = cv.VideoWriter("Recognition.avi", fourCC, 60.0, (640, 480))

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
        
    frame = cv.putText(frame, 
                       f"{len(faces)} face(s)!",
                       (50, 50),
                       cv.FONT_HERSHEY_SIMPLEX,
                       1,
                       (0, 0, 255),
                       2,
                       cv.LINE_AA)
    
    out.write(frame)
        
    cv.imshow("Screen", frame)
    
    if cv.waitKey(1) & 0xFF == 27:
        print("Video Recorded...")
        break
    
cam.release()
out.release()
cv.destroyAllWindows()
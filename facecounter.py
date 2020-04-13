import cv2
import datetime

file=open('counter1234.txt','w')
#otpt=""
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. Change VideoCapture vlaue from 1 to 0 if using built-in laptop webcam 
cap = cv2.VideoCapture(1)

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display
    cv2.imshow('img', img)
    count=str(len(faces))
    otpt = str('Time={}, Count={}'.format(datetime.datetime.now(),count))
    
    # Wirte into txt file
    file.write(otpt)
    file.write('\n')

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()

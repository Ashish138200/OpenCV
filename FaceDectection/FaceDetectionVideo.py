import cv2,time

# for webcam : 0
# external cam: 1
video = cv2.VideoCapture("face.mp4")
while(True):
    check, frame = video.read()
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    #print(check) # check if the video is running or not
    #print(frame) # numpy array
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        img = cv2.rectangle(frame, (x, y), (x + w, y + w), (0, 255, 0), 1)
    cv2.imshow("Capturing",frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows
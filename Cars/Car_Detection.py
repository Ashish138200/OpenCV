import cv2

video= cv2.VideoCapture("DataSet/video2.avi")
while True:
    check, frame = video.read()
    car_cascade = cv2.CascadeClassifier("cars.xml")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in cars:
        img = cv2.rectangle(frame, (x, y), (x + w, y + w), (0, 255, 0), 1)
    cv2.imshow("Detecting", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows
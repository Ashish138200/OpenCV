import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("photo.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.05,minNeighbors = 5)

# scaleFactor is telling python to decrease the scale by 5% for the next face search so on....Small scale have more accuracy
# minNeighbors tells python how many neighbors to search around the window

for x,y,w,h in faces:
    # 1. (x,y):starting point of the rectangle
    # 2. (x+w,y+w) : bottom right corner
    # 3. color(0:blue,255:green,0)
    # 4. width of rectangle
    img = cv2.rectangle(img,(x,y),(x+w,y+w),(0,255,0),3)
#print(type(faces))
#print(faces)

resized = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import glob # this finds the file names with certain patterns

images=glob.glob("sample_images\*.jpg")

for image in images:
    img=cv2.imread(image,1)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re) #new name
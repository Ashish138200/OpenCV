import cv2

'''
-1: Transparency
0: Black and white
1: Colourful
'''
img = cv2.imread("galaxy.jpg",0)
print(img.shape)
# print(img.ndim) # for checking dimensions
resize_img = cv2.resize(img,(990,1485))
cv2.imshow("Galaxy",resize_img)
cv2.imwrite("Galaxyresized.jpg",resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
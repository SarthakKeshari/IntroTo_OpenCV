import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')
kernel = np.ones((5,5),np.uint8)

#Gray Image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Blur Image
imgBlur = cv2.GaussianBlur(img,(7,7),0)

#Edge detector
imgCanny = cv2.Canny(img,200,200)

#Image dilation or edge thickner
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)

#Image erosion or edge thinner(opposite of image dilation)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)


cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dilation Image",imgDialation)
cv2.imshow("Erosion Image",imgEroded)
cv2.waitKey(0)
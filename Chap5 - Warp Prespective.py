import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width,height = 450,350

points1 = np.float32([[148,303],[613,414],[72,615],[540,731]])
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(points1,points2)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output Image",imgOutput)
cv2.waitKey(0)
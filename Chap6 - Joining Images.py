import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')

# #Horizontal stacking of Image
# imgHor = np.hstack((img,img))
# cv2.imshow("Horizontal",imgHor)
#
#
# #Vertical stacking of Image
# imgVer = np.vstack((img,img))
# cv2.imshow("Vertical",imgVer)

cv2.waitKey(0)
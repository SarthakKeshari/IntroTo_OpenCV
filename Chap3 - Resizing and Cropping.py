import cv2

img = cv2.imread('Resources/lambo.jpg')
print(img.shape)

# #Image Resizing
# imgResize = cv2.resize(img,(200,250))
# print(imgResize.shape)
# cv2.imshow("Resized Image",imgResize)

#Image Cropping
imgCropped = img[0:200,100:300]
cv2.imshow("Cropped Image",imgCropped)

cv2.imshow("Image",img)

cv2.waitKey(0)
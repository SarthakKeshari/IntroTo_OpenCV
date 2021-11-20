import cv2
import numpy as np

path = 'Resources/lambo.jpg'


#trackBars
def empty(a):
    pass


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640,240)
cv2.createTrackbar("Hue Min","TrackBars",17,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Saturation Min","TrackBars",100,255,empty)
cv2.createTrackbar("Saturation Max","TrackBars",255,255,empty)
cv2.createTrackbar("Value Min","TrackBars",59,255,empty)
cv2.createTrackbar("Value Max","TrackBars",255,255,empty)

while True:
    img = cv2.imread(path)
    img = cv2.resize(img, (200, 250))
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Saturation Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Saturation Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Value Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Value Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    imgHor = np.hstack((img,imgHSV,imgResult))
    cv2.imshow("Image", imgHor)
    cv2.imshow("Mask Image", mask)
    cv2.waitKey(1)
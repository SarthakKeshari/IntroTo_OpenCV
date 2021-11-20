import cv2
import numpy as np

def getContour(img):
    contours, hierarcy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgContour,cnt,-1,(255,255,0),3)
            peri = cv2.arcLength(cnt,True)
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            if objCor == 3: ObjectType = "Tri"
            elif objCor == 4:
                aspratio = w/float(h)
                if aspratio > 0.95 and aspratio < 1.05: ObjectType="Square"
                else: ObjectType="Rectangle"
            elif objCor>4: ObjectType = "Circle"
            else: ObjectType = "None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,ObjectType,((x+w//2)-10,(y+h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,0),1)





path = 'Resources/shapes.jpg'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)

getContour(imgCanny)

cv2.imshow("Original",img)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Shape Detect",imgContour)
cv2.waitKey(0)
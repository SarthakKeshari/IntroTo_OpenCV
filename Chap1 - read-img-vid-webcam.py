import cv2

# # Reading Image
# img = cv2.imread('Resources/lena.png')
#
# cv2.imshow("Output",img)
# cv2.waitKey(0)


# #Reading Video
# vid = cv2.VideoCapture("Resources/test_video.mp4")
#
# while True:
#     success, img = vid.read()
#     cv2.imshow('Video',img)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break


# #Using Webcam
# vid = cv2.VideoCapture(0)
# vid.set(3,640)
# vid.set(4,480)
# vid.set(10,100)
#
# while True:
#     success, img = vid.read()
#     cv2.imshow('Video',img)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
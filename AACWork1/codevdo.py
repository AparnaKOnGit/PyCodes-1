import cv2
x=cv2.VideoCapture(0)
while True:
    isTrue , frame=x.read()
    cv2.imshow('video',frame)
    if cv2.waitKey(2) & 0xFF==ord('a'):
        break
    
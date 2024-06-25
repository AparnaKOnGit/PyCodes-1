import cv2 
img =cv2.imread('image.jpg')
cv2.rectangle(img,(217,54),(411,219),(0,0,0),5)
cv2.circle(img,(163,98),40,(255,0,0),-1)
cv2.circle(img,(472,92),40,(255,0,0),-1)
cv2.putText(img,'Red-Tshirt',(192,38),cv2.FONT_HERSHEY_TRIPLEX,1.5,(0,150,255),5)
cv2.line(img,(177,48),(500,48),(0,0,255),2)
cv2.imshow('picture',img)
cv2.waitKey(0)
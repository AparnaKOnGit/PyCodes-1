import cv2
import numpy as np

def biggest_contour(contours):
    biggest=np.array([])
    max_area=0
    for i in contours:
        area=cv2.contourArea(i)
        if area > 500:
            peri = cv2.arcLength(i,True)
            approx= cv2.approxPolyDP(i, 0.02*peri ,True)
            print("points",len(approx))
            if area > max_area and len(approx) == 4:
                biggest=approx
                max_area=area
    print(biggest)
    return biggest       


img =cv2.imread("image_to_crop.jpg")
#image processing
img1=cv2.resize(img,(500,500))
gray=cv2.cvtColor(img1,cv2.COLOR_RGB2GRAY)
gray=cv2.bilateralFilter(gray,20,30,30)
edge=cv2.Canny(gray,150,200)


#contours
contours,hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours=sorted(contours,key=cv2.contourArea,reverse=True)[:1]
biggest=biggest_contour(contours)
cv2.drawContours(img,[biggest], -1, (10, 220,180), 5)


cv2.imshow("original",img1)



points=biggest.resize(4,2)
input_points=np.zeros((4,2),dtype="float32")


points_sum=points.sum(axis)
cv2.imshow("image",img)
cv2.waitKey(0)

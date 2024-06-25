import cv2
import numpy as np
img = cv2.imread('image_to_crop.jpg')
img1=cv2.resize(img,(500,500))
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
edge=cv2.Canny(gray,150,200)
contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_image= np.zeros_like(img1)

#drawing contours 
cv2.drawContours(contour_image, contours, -1, (10, 220,180), 7)
combined_image=cv2.bitwise_or(img1,contour_image)
cv2.imshow("Lined Document",contour_image)


#cropping 
dst = cv2.cornerHarris(gray, 2, 3, 0.04)


# Dilate the corner points to make them more visible
dst = cv2.dilate(dst, None)


# Threshold the corner response
threshold = 0.01 * dst.max()
corner_image = np.zeros_like(img1)
corner_image[dst > threshold] = [0, 0, 255]
cv2.imshow('Detected Corners', corner_image)
#cv2.imshow("cropped",cropped_image)


cv2.waitKey(0)
import cv2
import numpy as np
img =cv2.imread('paper_img.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
edge=cv2.Canny(gray,150,200)
#/////////////////////////#
contours, _ = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest_contour = max(contours, key=cv2.contourArea)
epsilon = 0.02 * cv2.arcLength(largest_contour, True)
approx = cv2.approxPolyDP(largest_contour, epsilon, True)
if len(approx) == 4:
    bounding_box = cv2.boundingRect(approx)
x, y, w, h = bounding_box
cropped_image = img[y:y + h, x:x + w]
points = approx.reshape(4, 2)
output_width, output_height = (400, 500)  
dst_points = np.array([
    [0, 0],
    [output_width, 0],
    [output_width, output_height],
    [0, output_height]
], dtype="float32")
matrix = cv2.getPerspectiveTransform(points.astype("float32"), dst_points)
corrected_image = cv2.warpPerspective(img, matrix, (output_width, output_height))
cv2.imwrite("cropped_document.jpg", corrected_image)
cv2.imshow("Cropped Document", corrected_image)
cv2.waitKey(0)
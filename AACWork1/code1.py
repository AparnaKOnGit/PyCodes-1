import cv2

img = cv2.imread('ye.jpg')

if img is None:
    print(f'Error reading image...')
else:
    print("Image read!")
    cv2.imshow('Ye', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
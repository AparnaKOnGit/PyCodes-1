import cv2

print("Using cv2 to work with images...")

img_path = './img.jpg'
my_img = cv2.imread(img_path)

if my_img is None:
    print(f'Error Reading Image {img_path}')
else:
    print("Image read...")
    cv2.imshow('Picture1', my_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




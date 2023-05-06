import cv2

path = r'C:\Users\Hungd\Downloads\rgb.jpg'

img = cv2.imread(path)

b, g, r = cv2.split(img)

cv2.imshow('blue', b)

if cv2.waitKey() == ord('b'):
    cv2.destroyAllWindows()


import cv2


path = r'C:\Users\Hungd\Downloads\rgb.jpg'

img = cv2.imread(path)


B, G, R = cv2.split(img)

cv2.imshow('anh goc', img)
cv2.imshow('red', R)
cv2.imshow('green', G)
cv2.imshow('blue', B)

cv2.waitKey()
import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

img = cv2.imread(path)

Ie = cv2.Canny(image = img, threshold1 = 160, threshold2 = 326)

cv2.imshow('anhnhiphan', Ie)

if Ie[160, 326] == 255 :
    print('Diem nay la diem bien cua anh img theo pp do bien canny')
else :
    print('Diem nay khong phai la diem bien cua anh img theo pp do bien canny')

cv2.imshow('anhimg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
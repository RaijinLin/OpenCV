import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'


I = cv2.imread(path)
Ig = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

Icanny = cv2.Canny(image=Ig, threshold1=100, threshold2=200)
cv2.imshow('Icanny', Icanny)

if Icanny[100, 300] == 255:
    print("Pixel co toa do dong y=100, cot x=300 la diem bien cua anh")
else:
    print("Pixel co toa do dong y=100, cot x=300 khong phai la diem bien cua anh")

cv2.waitKey(0)
cv2.destroyAllWindows()

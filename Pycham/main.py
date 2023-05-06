import cv2
import os
path = r'C:\Users\Hungd\Downloads\meo.jpg'
path1 = r'C:\Users\Hungd\Downloads'

img = cv2.imread(path)

#cv2.imshow('tai anh', img)

fileName = 'anhmeo2.jpg'

os.chdir(path1)
cv2.imwrite(fileName, img)
print('luu anh thanh cong')



cv2.waitKey(3000)
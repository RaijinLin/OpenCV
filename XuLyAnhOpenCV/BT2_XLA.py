import cv2
from cv2 import COLOR_BGR2GRAY
import numpy as np

I = cv2.imread('G:\XuLyAnhOpenCV\ThoNgoc.jpg')

cv2.imshow('Original image',I)

#Cach 1: sử dụng hàm có sẵn OpenCV (I_gray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)  )
I_gray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) 
cv2.imshow('Color image', I_gray)

#Cach 2: Viet ham
def xuatAnhGray(I):
  I_gray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
  return I_gray
E = cv2.imread('G:\XuLyAnhOpenCV\Dep.jpg')
cv2.imshow('Color',E)

cv2.imshow('Color IMG', xuatAnhGray(E))

#Cach 2: Viet ham Y = 0.2126R + 0.7152G + 0.0722B
from PIL import Image
img = Image.open('G:\XuLyAnhOpenCV\ThoNgoc.jpg')
pixels = img.load()

new_img = Image.new(img.mode, img.size)
pixels_new = new_img.load()
for i in range(new_img.size[0]):
    for j in range(new_img.size[1]):
        r, b, g = pixels[i,j]
        avg = int(round((0.2126*r + 0.0722*b + 0.715*g) / 3))
        pixels_new[i,j] = (avg, avg, avg, 0)
new_img.show()

#cách khác viết hàm
b, r, g = cv2.split(I)
I_gray2 = cv2.cvtColor(I, COLOR_BGR2GRAY)
I_gray2 = (0.2126*r + 0.0722*b + 0.715*g).astype(np.uint8)
cv2.imshow('Img gray', I_gray2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

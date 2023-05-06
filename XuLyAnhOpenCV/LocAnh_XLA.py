import cv2
import numpy as np

I = cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\I04.jpg')
cv2.imshow('Colors',I)

#Lọc trung bình
Ir,Ig,Ib=cv2.split(I)

h = I.shape[0]
w = I.shape[1]

#cap phat anh RGB moi
I_avg=np.zeros((h,w,3),dtype='uint8')
I_avg[:,:,2]=cv2.blur(Ir,(3,3))
I_avg[:,:,1]=cv2.blur(Ig,(3,3))
I_avg[:,:,0]=cv2.blur(Ib,(3,3))

cv2.imshow('Loc trung binh',I_avg)

I2 = cv2.imread('G:\XuLyAnhOpenCV\ThoNgoc.jpg')
cv2.imshow('Anh goc',I2)

Ir,Ig,Ib=cv2.split(I2)

h = I2.shape[0]
w = I2.shape[1]

#lọc median (trung vị)
I_med=np.zeros((h,w,3),dtype='uint8')
I_med[:,:,2]=cv2.medianBlur(Ir,3)
I_med[:,:,1]=cv2.medianBlur(Ig,3)
I_med[:,:,0]=cv2.medianBlur(Ib,3)

cv2.imshow('Loc trung vi',I_med)

#Lọc trọng số
import random
matran_trongso= np.zeros((7,7),dtype='float32')
s=0.0
for i in range(7):
    for j in range(7):
        matran_trongso[i][j]=random.random()
        s=s+matran_trongso[i][j]

for i in range(7):
    for j in range(7):
        matran_trongso[i][j]=matran_trongso[i][j]/s

print(matran_trongso)
I_2 = cv2.filter2D(I,-1,matran_trongso)

if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
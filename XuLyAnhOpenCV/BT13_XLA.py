import cv2
I = cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\den5.jpg')
cv2.imshow('Colors',I)

# 13a. Xác định dải giá trị xám của kênh R của I: a=min(R), b=max(R)
import numpy as np
Ir, Ig, Ib = cv2.split(I)
print("Giá trị mức xam min(R)={}, max(R)={}".format(np.min(Ir), np.max(Ir)))

# 13b. Biến đổi mức xám của kênh R sao cho a=0, b=255 (tăng dải động lên)
h = I.shape[0]
w = I.shape[1]
a = 0
b = 255
for i in range(h):
    for j in range(w):
        Ir[i][j]=(255* int(Ir[i][j]-a))//(b-a)
cv2.imshow('Kenh R bien doi', Ir)

# 13c. Biến đổi tương tự với kênh G và kênh B.
for i in range(h):
    for j in range(w):
        Ir[i][j]=(255* int(Ir[i][j]-a))//(b-a)
cv2.imshow('Kenh G bien doi', Ig)

for i in range(h):
    for j in range(w):
        Ir[i][j]=(255* int(Ir[i][j]-a))//(b-a)
cv2.imshow('Kenh B bien doi', Ib)

#Cach khac
a1 = np.min(Ir)
b1 = np.max(Ir)
 
a2 = np.min(Ig)
b2 = np.max(Ig)
 
a3 = np.min(Ib)
b3 = np.max(Ib)
   
print('Mức xám a1, b1: ', a1, b1)
 
(row, col) = I.shape[0:2]
for i in range(row):
    for j in range(col):
        Ir[i][j] = (255 * int(Ir[i][j]-a1))//(b1-a1)
        Ig[i][j] = (255 * int(Ig[i][j]-a2))//(b2-a2)
        Ib[i][j] = (255 * int(Ib[i][j]-a3))//(b3-a3)
 
 
cv2.imshow('Kenh R bien doi', Ir)
cv2.imshow('Kenh G bien doi', Ig)
cv2.imshow('Kenh B bien doi', Ib)

if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
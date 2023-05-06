import cv2

# Bài 14. Đọc vào bộ nhớ ảnh I04.jpg, được ma trận ảnh I.
I=cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\I04.jpg')
cv2.imshow('Colors',I)

# Xác định histogram của kênh R,G và B của ảnh I, bằng cách tự viết code
import numpy as np
import matplotlib.pyplot as plt
Ib,Ig,Ir = cv2.split(I)
def tinh_hist(Ig):
  a=np.zeros(256,dtype='int')
  h=Ig.shape[0]
  w=Ig.shape[1]
  for i in range(h):
      for j in range(w):
            g=Ig[i][j]
            a[g]=a[g]+1
  return a

print('Kênh B')
IB=I[:,:,0]
hB=tinh_hist(IB)

plt.plot(hB)
plt.show()

print('Kênh G')
IG=I[:,:,1]
hG=tinh_hist(IG)

plt.plot(hG)
plt.show()

print('Kênh R')
IR=I[:,:,2]
hR=tinh_hist(IR)

plt.plot(hR)
plt.show()

# 14a.1. Xác định histogram của kênh R,G và B của ảnh I, bằng thư viện cv2 và tự viết hàm 
print('Sử dụng thư viện vẽ hist kênh B')
hB_ = cv2.calcHist([IB],[0],None,[256],[0,256])
plt.plot(hB_)
plt.show()

print('Sử dụng thư viện vẽ hist kênh G')
hG_ = cv2.calcHist([IG],[0],None,[256],[0,256])
plt.plot(hG_)
plt.show()

print('Sử dụng thư viện vẽ hist kênh R')
hR_ = cv2.calcHist([IR],[0],None,[256],[0,256])
plt.plot(hR_)
plt.show()

# 14b. Cân bằng histogram của kênh R,G và B.
I_new=I.copy()
I_new[:,:,0]= cv2.equalizeHist(I[:,:,0])
print('Can bang kenh B')
cv2.imshow('Can bang kenh B',I_new[:,:,0])
I_new[:,:,1]= cv2.equalizeHist(I[:,:,1])

print('Can bang kenh G')
cv2.imshow('Can bang kenh G',I_new[:,:,1])
I_new[:,:,2]= cv2.equalizeHist(I[:,:,2])

print('Can bang kenh R')
cv2.imshow('Can bang kenh R',I_new[:,:,2])

# Hiển thị ảnh kết quả.
print('Anh RGB sau khi can bang')
cv2.imshow('Anh sau khi can bang',I_new)

if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
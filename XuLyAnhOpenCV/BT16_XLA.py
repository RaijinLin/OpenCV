import cv2
import numpy as np
import matplotlib.pyplot as plt

#Bài tập 16. Đọc vào ảnh grayscale 5.jpg
I = cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\den5.jpg')
cv2.imshow('Colors',I)

#16a. Xác đinh và vẽ histogram của ảnh. (dùng hàm có sẵn hoặc viết hàm) 
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

#16b. Nhận xét gì về histogram của ảnh.
# Câu1: Đen trắng, trắng tuyệt đối có tập giá trị là{255} hoặc {0,255},{0}<{255}

# Câu2: Đen trắng, đen tuyệt đối có tập giá trị là{0} hoặc {0,255},{0}>{255}

# Câu3: Ảnh grayscale rất tối thì khi vẽ biểu đồ histogram sẽ phân bố về phía trục gốc (gần về 0)

# Câu4: Ảnh grayscale độ tương phản thấp thì khi vẽ biểu đồ histogram phân bố không đều, histogram phân bố ở giữa.

# Câu5: Ảnh grayscale độ tương phản cao thì khi vẽ biểu đồ histogram phân bố đều

#16c. Cân bằng histogram của ảnh.  (equalizeHist)
I_new=I.copy()
I_new[:,:,0]= cv2.equalizeHist(I[:,:,0])
print('Can bang kenh B')
cv2.imshow('Can bang kenh B', I_new[:,:,0])
I_new[:,:,1]= cv2.equalizeHist(I[:,:,1])

print('Can bang kenh G')
cv2.imshow('Can bang kenh G', I_new[:,:,1])
I_new[:,:,2]= cv2.equalizeHist(I[:,:,2])

print('Can bang kenh R')
cv2.imshow('Can bang kenh R', I_new[:,:,2])

#16d. Hiển thị ảnh sau khi cân bằng histogram
print('Anh RGB sau khi can bang')
cv2.imshow('Anh sau khi can bang', I_new)

if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
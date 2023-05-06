import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. Đọc ảnh mầu hat1.png vào biến ma trận I. Hiển thị ảnh I.
I = cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\hat1.PNG')
cv2.imshow('Colors',I)

#2. Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh V của Ihsv.
#Xác định giá trị mức sáng lớn nhất của kênh H của ảnh Ihsv.
Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
H = Ihsv[:,:,0]
S = Ihsv[:,:,1]
print("Kênh V")
cv2.imshow('Kênh V', Ihsv[:,:,2])
print("Giá trị mức sáng lớn nhất: ", H.max())

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("Anh HSV 1", Ihsv)
 
# Hiển thị kênh V của Ihsv.
cv2.imshow('Kenh V',Ihsv[:,:,2])

# Xác định giá trị mức sáng lớn nhất của kênh H của ảnh Ihsv.
(H,S,V) = cv2.split(Ihsv)
H1 = np.array(H)
maxH = H1.max()
print("Mức sáng lớn nhất của kênh H: ", maxH)

#3. Vẽ histogram của kênh S của ảnh Ihsv.
#Cach 1:
def tinh_hist(Ig):
  a=np.zeros(256,dtype='int')
  h=Ig.shape[0]
  w=Ig.shape[1]
  for i in range(h):
      for j in range(w):
            g=Ig[i][j]
            a[g]=a[g]+1
  return a

print('Kênh S')
hB=tinh_hist(S)
plt.plot(hB)
plt.show()

#Cach khac:
hS_ = cv2.calcHist([Ihsv],[1],None,[256],[0,256])
plt.plot(hS_,color="Black")
plt.show()


#4. Làm trơn ảnh kênh S của Ihsv theo bộ lọc median, kích thước cửa sổ lân cận là 5x5 được ảnh Is. Hiển thị ảnh Is.
#Cach 1:
img_median=cv2.medianBlur(S,5)
cv2.imshow('Median', img_median)

#Cach khac:
median = cv2.medianBlur(Ihsv[:,:,1],5)
cv2.imshow('Loc median S',median)

# 5. Xác định đường contour có chu vi lớn nhất của ảnh Ib. Vẽ đường contour trên ảnh gốc I. Hiển thị ảnh I.
img_gray=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
ret, img_binary = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
# img_binary=255-img_binary
cv2.imshow('Binary', img_binary)

contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max_area=0.0
for cnt in contours:
    if max_area < cv2.contourArea(cnt):
        max_area=cv2.contourArea(cnt)
for cnt in contours:
    if cv2.contourArea(cnt) > max_area/2:
        cv2.drawContours(I,[cnt],-1,(0,255,0),2)
cv2.imshow('Contours',I)

max_cv = 0
cnt_max = []
for cnt in contours:
    if cv2.arcLength(cnt, True) > max_cv:
        max_cv = cv2.arcLength(cnt, True)
        cnt_max = cnt
print("Chu vi lớn nhất: " ,max_cv)
cv2.drawContours(I, [cnt_max], -1, (0,255,0), 3)

if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
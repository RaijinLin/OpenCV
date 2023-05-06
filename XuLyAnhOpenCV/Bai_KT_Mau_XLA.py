import cv2
import numpy as np

# 1.  Đọc và hiển thị ảnh I.
I = cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\Coins.jpg')
cv2.imshow('Colors',I)

#2. Chuyển ảnh mầu I sang ảnh đa cấp xám (grayscale) theo công thức (0.39,0.5,0.11), được ma trận ảnh Ig. Hiển thị ảnh Ig. Xác định mức xám lớn nhất của ảnh Ig.
Ig = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) 
cv2.imshow('Gray',Ig)
B, G, R = I[:,:,0], I[:,:,1], I[:,:,2]
Ig1 = 0.11 * B + 0.5 * G + 0.39 * R
cv2.imshow('Gray 1', Ig1)
print('Mức xám lớn nhất: ', Ig1.max())

# 3. Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên Ie là ảnh nhị phân nền đen. Kiểm tra pixel có tọa độ dòng y=160, cột x=326 có là điểm biên của ảnh Ig theo phép dò biên Canny không?
Ibl = cv2.blur(Ig,(3,3)) 
Ie = cv2.Canny(Ibl, threshold1=100, threshold2=200) 
cv2.imshow('Cany', Ie)
print('Pixel có tọa độ dòng y=160, cột x=326 có là điểm biên của ảnh Ig theo phép dò biên Canny ',Ie[10][32])
print('Khong kiem tra pixel có tọa độ dòng y=160, cột x=326 có là điểm biên của ảnh Ig theo phép dò biên Canny vi diem bien phai mau trang la =1 con = 0 la sai ')
# 3.1. Xác định ma trận gradient theo hướng y và theo hướng x của Ig sử dụng toán tử Sobel và hiển thị 2 ma trận kết quả. 
sobelx = cv2.Sobel(I,ddepth=cv2.CV_64F, dx=1, dy=0, ksize=1)  
sobely = cv2.Sobel(I,cv2.CV_64F,0,1,ksize=1)  
cv2.imshow('Sobel x', sobelx)
cv2.imshow('Sobel y', sobely)

# 4.  Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen được ảnh Ib. Hiển thị ảnh Ib.
threst, Ib = cv2.threshold(Ig, 500, 255, cv2.THRESH_OTSU)
cv2.imshow('Nguong Otsu', Ib)

# 5. Xác định các đường contour của ảnh Ib, tìm giá trị max_cv là chu vi lớn nhất trong các contour trên. Vẽ các contours có chu vi lớn nhất lên ảnh gốc I với mầu bgr = (0,0,255). Hiển thị ảnh I.
I_copy = I.copy()
contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I_copy   , contours, -1, (0,255,0), 3) #vẽ trên ảnh gốc
cv2.imshow('Copy', I_copy)

I_copy1 = I.copy()
for contour in contours:
  if cv2.contourArea(contour) > 200: #thay đổi 200 ở đây để lọc contour
      cv2.drawContours(I_copy1, [contour], -1, (0,0,255), 3)
cv2.imshow('Copy 1', I_copy1)

if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
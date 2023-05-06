import cv2

#đọc ảnh và hiển thị hình ảnh
I = cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\CMTND01.jpg')
cv2.imshow('Original image', I)

# 4a. Hiển thị giá trị pixel điểm ảnh tại tọa độ y=40 (dòng), x=15 (cột).
print(' Pixel (15,40 hàng r = )', I[40,15,0])
print(' Pixel (15,40 hàng b = )', I[40,15,1])
print(' Pixel (15,40 hàng g = )', I[40,15,2])
print(' Pixel (15,40) = ', I[40, 15])

# 4b. Nhị phân hóa ảnh đã đọc theo ngưỡng
I_gray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) 
cv2.imshow('Color image',I_gray)

# 4b1. Ngưỡng quyết định nhị phân 90
threshold , I_baclkwhite= cv2.threshold(I_gray, 90, 255, cv2.THRESH_BINARY)
cv2.imshow('Color binary',I_baclkwhite)
print(' Pixel (15,40) = ', I_baclkwhite[40][15])

# 4b2. Ngưỡng quyết định nhị phân theo Otsu
threshold, I_baclkwhite2 = cv2.threshold(I_gray,125,255,cv2.THRESH_OTSU)
cv2.imshow('Color otsu',I_baclkwhite)

# Hiển thị giá trị pixel điểm ảnh tại tọa độ y=40 (dòng), x=15 (cột) của ảnh nhị phân tương ứng.
print(' Pixel (15,40) = ', I_baclkwhite2[40][15])

# # 4c. Chuẩn hóa bảo toàn tỉ lệ ảnh mầu đã đọc theo size 300 x 500)
I_new=cv2.resize(I,(500,300))
cv2.imshow('Size',I_new)

#ghi kết quả thành file ảnh CMND01_300_500.png (định dạng nén png)
cv2.imwrite('G:\XuLyAnhOpenCV\CMND01_300_500.png',I_new)

# 4d. Tính min, max giá trị mức xám của kênh Red của ảnh câu 4a.
import numpy as np
(R,B,G)=cv2.split(I)
print("Giá trị mức xám min(R) = {}, max(R) = {}".format(np.min(R), np.max(R)))

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
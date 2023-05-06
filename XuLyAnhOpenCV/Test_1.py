import cv2
import numpy as np
from cv2 import COLOR_BGR2GRAY

#1. Đọc 1 ảnh vào biến bộ nhớ, hiển thị ảnh
img = cv2.imread('G:\XuLyAnhOpenCV\ThoNgoc.jpg',1)
cv2.imshow('Colors',img)

#2. Hiện thị chiều cao, chiều rộng, số kênh của ảnh
print('Chiều rộng, Chiều cao, Số kênh: ',img.shape)

#3.  Hiển thị ảnh tung kenh
(r,g,b)=cv2.split(img)
cv2.imshow('Red',r)
cv2.imshow('Green',g)
cv2.imshow('Blue',b)

#Hien thi anh kenh B
cv2.imshow('Kenh B: ', img[:, :, 2])

#4. Hiển thị kích thước ảnh
print('Kích thước ảnh: ', img.size)

#5. Resize ảnh nhỏ bằng 1/2 ảnh ban đầu
#Cach 1
scale_percent = 50
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dsize = (width, height)
output = cv2.resize(img, dsize)
print('Size = ',output.size)
cv2.imshow('Resize',output)

#cach 2
w = int(img.shape[1]/2)
h = int(img.shape[0]/2)
dim = (w,h)
half = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized image", half)

#6. Chuyển ảnh kênh R sang ảnh đen trắng với ngưỡng 150. Hiển thị.
(T, threshInv) = cv2.threshold(r, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Binary", threshInv)

#7. Tách lấy kênh R của ảnh. Chuyển ảnh kênh R sang ảnh trắng đen với ngưỡng 90
imgR = img[:,:,2]
cv2.threshold(imgR,90,255,cv2.THRESH_BINARY)
cv2.imshow('Image red',imgR)

# 6. Tách 3 kênh của ảnh I thành I_red, I_green, I_blue. Hiển thị ảnh kênh I_blue.
imgR = img[:,:,2]
imgG = img[:,:,1]
imgB = img[:,:,0]
cv2.imshow('Blue chanel', imgB)

# 7. Hiển thị giá trị pixel điểm ảnh tại tọa độ y=40 (dòng), x=15 (cột) của ảnh I_blue.
print(' Pixel (15,40)=', imgB[40][15])

# 8. Tính min, max giá trị mức xám của kênh green 
(R,B,G)=cv2.split(img)
print("Giá trị mức xám max = ", imgG.max())
print("Giá trị mức xám min = ", imgG.min())

# 9. Chuyển I thành ảnh xám I_gray sử dụng hàm có sẵn trong OpenCV. 
I_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
cv2.imshow('Color image', I_gray)

# 10. Chuyển I thành ảnh xám I_gray2 bằng cách tự viết hàm. 
# Công thức chuyển Y = 0.2126R + 0.7152G + 0.0722B
b, r, g = cv2.split(img)
I_gray2 = cv2.cvtColor(img, COLOR_BGR2GRAY)
I_gray2 = (0.2126*r + 0.0722*b + 0.7152*g).astype(np.uint8)
cv2.imshow('Img gray', I_gray2)

# 11. Tính min, max giá trị mức xám của ảnh I_gray
(R,B,G)=cv2.split(img)
print("Giá trị mức xám max = ", I_gray.max())
print("Giá trị mức xám min = ", I_gray.min())

# 12. Hiển thị giá trị pixel điểm ảnh tại tọa độ y=40 (dòng), x=15 (cột) của ảnh  I_gray2. 
print(' Pixel (15,40) = ', I_gray2[40][15])

# 13. Chuyển I_gray thành ảnh trắng đen I_bw với ngưỡng 90. Điều chỉnh ngưỡng (bằng 50 và 120),  hiển thị ảnh. 
I_bw, threshold = cv2.threshold(I_gray, 90, 255, cv2.THRESH_BINARY)
I_bw1, threshold = cv2.threshold(I_gray, 50, 120, cv2.THRESH_BINARY)
cv2.imshow('Color binary',threshold)

# 14. Chuyển I_red thành ảnh trắng đen I_bw2 với ngưỡng OTSU. Hiển thị ảnh và ngưỡng tìm được. 
threshold, I_bw2 = cv2.threshold(imgR,125,255,cv2.THRESH_OTSU)
cv2.imshow('Color otsu',threshold)

# 15. Chuyển I_gray thành ảnh trắng đen I_bw3 với ngưỡng GAUSSIAN ….  
I_bw3 = cv2.GaussianBlur(I_gray, (7, 7), 0)
cv2.imshow('Gaussian', I_bw3)

# 16. Tính min, max giá trị mức xám của ảnh I_bw
(R,B,G)=cv2.split(img)
print("Giá trị mức xám max = ", np.max(I_bw))
print("Giá trị mức xám min = ", np.min(I_bw))

# 17. Hiển thị giá trị pixel điểm ảnh tại tọa độ y=40 (dòng), x=15 (cột) của ảnh  I_bw2.
print(' Pixel (15,40) = ', I_bw2[40][15])

#Thoát bằng esc
if cv2.waitKey(0) &0xff == 27:
 cv2.destroyAllWindows()

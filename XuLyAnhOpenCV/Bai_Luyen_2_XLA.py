import cv2
import numpy as np
import matplotlib.pyplot as plt

#1. hiện thị ảnh anh2.jpg gán vào I
I = cv2.imread("Untitled.jpg")
cv2.imshow('#1: Colors', I)

#2. Viết hàm chuyển I thành ảnh đa cấp xám theo tỷ lệ (0.39,0.5,0.11), được ma trận ảnh Ig. Xác định mức xám lớn nhất và mức xám trung bình của ảnh Ig.
#Cach 1:
Ig = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) 
B, G, R = I[:,:,0], I[:,:,1], I[:,:,2]
Ig1 = 0.11 * R + 0.5 * G + 0.39 * B
cv2.imshow('#2.1: Gray', Ig1)

#Cach 2:
B,G,R = cv2.split(I)
I_gray = (0.39 * B + 0.5 * G + R * 0.11).astype(np.uint8)
cv2.imshow("#2.2: Gray",I_gray)

print('Mức xám lớn nhất: ', np.max(Ig1))
#mức xám trung bình của ảnh Ig.
minIg = np.min(Ig1)
maxIg = np.max(Ig1)
MucSangTB = (minIg+maxIg)//2
print('Giá trị mức sáng tb của V là: ',MucSangTB)

#3. Xác định ma trận gradient theo hướng y và theo hướng x của Ig sử dụng toán tử Sobel và hiển thị 2 ma trận kết quả.
Ibl = cv2.blur(Ig,(3,3)) #lọc ảnh trung bình
Iga = cv2.GaussianBlur(Ibl,(5,5),0) #lọc ảnh Gaussian 
img_sobelx = cv2.Sobel(Iga,ddepth=cv2.CV_64F, dx=1, dy=0, ksize=1)  # tìm biên sobel đạo hàm theo x
img_sobely = cv2.Sobel(Iga,cv2.CV_64F,0,1,ksize=1)  #  tìm biên sobel đạo hàm the y

img_sobelx = np.uint8(np.absolute(img_sobelx))
img_sobely = np.uint8(np.absolute(img_sobely))

img_sobel = (img_sobelx + img_sobely)/2
for i in range(img_sobel.shape[0]):
    for j in range(img_sobel.shape[1]):
        if img_sobel[i][j] < 25:
            img_sobel[i][j] = 0
        else:
            img_sobel[i][j] = 255

cv2.imshow('#3:Sobel x', img_sobelx)
cv2.imshow('#3:Sobel y', img_sobely)
cv2.imshow('#3:Sobel', img_sobel)
print(img_sobelx)
print(img_sobely)

#.4 Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên Ie là ảnh nhị phân nền đen. Hiển thị các độ xám của của cửa sổ lân cận 3x3 của pixel có tọa độ dòng y=78, cột x=23 của ảnh Ig.
#Cach 1:
Ie = cv2.Canny(Ibl, threshold1=100, threshold2=200) # tìm biên theo Canny 
cv2.imshow('#4:Ie', Ie)
print(' y=78, cột x=23 ', Ig[78][23])

#Cach khac:
I_gray = cv2.cvtColor(I, cv2.COLOR_RGBA2GRAY)
I_blur = cv2.blur(I_gray,(3,3))
 
I_canny = cv2.Canny(image=I_blur, threshold1=100, threshold2=200)
cv2.imshow('#4:Icanny',I_canny)

#5. Nhị phân ảnh Ig với ngưỡng 150 được ảnh nhị phân nền đen Ib. Chuyển thành ảnh nền đen. Xác định các đường contour của ảnh Ib. Loại các countour bé. Vẽ các đường contour trên lên ảnh gốc I.
ret, Ib = cv2.threshold(Ig, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('#5:Nhi phân', Ib)
I_copy = I.copy()
contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I_copy, contours, -1, (0,0,255), 3) #vẽ trên ảnh gốc
cv2.imshow('#5:Copy', I_copy)
max_cv = 0
for cnt in contours:
    if cv2.arcLength(cnt, True) > max_cv:
        max_cv = cv2.arcLength(cnt, True)
print("Chu vi lon nhat", max_cv)
for contour in contours:
    if cv2.contourArea(contour) >= max_cv:
        cv2.drawContours(I, [contour], -1, (0, 255, 0), 3)

if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
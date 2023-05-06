import cv2
import numpy as np
# 1. Đọc ảnh  I. Hiển thị ảnh I.
I = cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\Pic5.jpg')
cv2.imshow('Original', I)

# 2. Chuyển ảnh mầu I sang ảnh đa cấp xám với thành phần mầu (r,g,b) là  (0.39,0.5,0.11), được ma trận ảnh Ig. Hiển thị Ig. Tính mức xám trung bình của Ig.
def cvtGray(I):
    grayColor = 0.39 * I[:, :, 2] + 0.5 * I[:, :, 1] + 0.11 * I[:, :, 0]
    grayColor = grayColor.astype(dtype='uint8')
    return grayColor

Ig = cvtGray(I)
cv2.imshow('Gray Img', Ig)
print('Mean Gray : ', Ig.mean())

# 3. Chuyển  I sang dạng HSV được ảnh Ihsv. Xác định mức xám lớn nhất của kênh S của Ihsv.
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow('Kenh S', Ihsv[:,:,1])
Ihsv_s = Ihsv[:, :, 1]
print('Mức xám lớn nhất kênh S : ', np.max(Ihsv[:,:,1]))

# 4. Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen được ảnh Ib. Hiển thị ảnh Ib.
thresh, Ib = cv2.threshold(Ig, 180, 255, cv2.THRESH_OTSU)
cv2.imshow('Binary Img', Ib)

# 5. Xác định  contour của Ib, tìm giá trị max của contour có chu vi lớn nhất. Vẽ các contours có chu vi > max/5 lên ảnh gốc I với mầu (255,0,255). Hiển thị.
I_copy = I.copy()
contours, hie = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('Ib contours : ', contours)
cv2.drawContours(I_copy, contours, -1, (0, 0, 255), 2)

I_copy = I.copy()
max_cv = 0.0
Ib=255-Ib

#Cach 1:
for cnt in contours:
    if max_cv < cv2.arcLength(cnt, True):
        max_cv = cv2.arcLength(cnt, True)
print('Max CV : ',  max_cv)

for cnt in contours:
    if cv2.arcLength(cnt, True) > max_cv/5:
        cv2.drawContours(I_copy, cnt, -1, (255,0,255), 2)
cv2.imshow('Draw Contours', I_copy)

#Cach 2:
i=0.0
for j in contours:
    chuvi = cv2.arcLength(j, True)
if(chuvi>i):
    i=chuvi
print("chu vi lon nhat cua cac contours la :",i)
for contour in contours:
    if cv2.arcLength(contour,True) == i/5:
        cv2.drawContours(I_copy, [contour], -1, (255,0,255), 3)
cv2.imshow('Contours',I_copy)

if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
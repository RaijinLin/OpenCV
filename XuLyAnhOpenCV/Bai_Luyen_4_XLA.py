import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh mầu anh5.jpg vào biến ma trận I.
# 1. Hiển thị I, kích thước của ảnh
I = cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\Pic5.jpg')
h,w,a=I.shape
cv2.imshow('Colors', I)
print("h={},w={},kenh={}".format(h,w,a))

# 2. Resize lại ảnh I cho kích thước tăng gấp đôi
h_new=h*2
w_new=w*2
Iresize=cv2.resize(I,(w_new,h_new))
cv2.imshow('Resize', Iresize)

# 3. Chuyển I sang HSV thành Ihsv. Làm trơn ảnh kênh S của Ihsv theo bộ lọc trung bình cộng, kích thước cửa sổ lân cận là 5x5 được ảnh Is. Hiển thị ảnh Is.
Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
H,S,V=cv2.split(Ihsv)
Sblur=cv2.blur(S,(5,5))
cv2.imshow('Kenh S', Sblur)

# 4. Nhị phân hóa ảnh bằng 255- Is (ảnh nghịch đảo) theo ngưỡng Otsu được ảnh nhị phân Ib. Xác định đường contour có chu vi lớn nhất của ảnh Ib. Vẽ đường contour trên ảnh gôc I.
otsu,I_otsu=cv2.threshold(Sblur,50,255,cv2.THRESH_OTSU)
Icopy=I.copy()
img_otsu=255-I_otsu
cv2.imshow('Otsu', img_otsu)
contours, hierarchy = cv2.findContours(img_otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max_area=0
for contour in contours:
    if max_area < cv2.contourArea(contour):
        max_area=cv2.contourArea(contour)
for contour in contours:
    if cv2.contourArea(contour) > max_area/2:
        cv2.drawContours(Icopy,[contour],-1,(0,255,0),2)
cv2.imshow('Copy', Icopy)

max_cv = 0
for cnt in contours:
   if cv2.arcLength(cnt, True) > max_cv:
       max_cv = cv2.arcLength(cnt, True)
print("Chu vi lon nhat", max_cv)
for contour in contours:
   if cv2.contourArea(contour) >= max_cv:
       cv2.drawContours(I, [contour], -1, (0, 255, 0), 3) #(img, contours, contourIdx, colour, thickness)
cv2.imshow('Anh contours ', I)

# 5.  Tăng độ sáng của kênh V của ảnh Ihsv bằng phương pháp giãn tuyến tính giá trị mức xám. Biến đổi ngược ảnh Ihsv về biểu diễn mầu RGB được ảnh I. Hiển thị lại ảnh I.
#Cach 1:
def hieuchinh_gamma(Igray, gamma = 1.0):
    w=Igray.shape[1]
    h=Igray.shape[0]

    Igray_new=np.zeros((h,w),dtype='uint8')
    for i in range(h):
        for j in range(w):
            g_f=float(Igray[i][j])/255.0
            g_f_new=np.power(g_f, gamma)
            g_new=int(g_f_new*255.0)
            Igray_new[i][j]=g_new
    return Igray_new
Iv=Ihsv[:,:,0]
V=hieuchinh_gamma(Iv,0.5)
cv2.imshow('Kenh V', V)
img_hsv_bgr=cv2.cvtColor(Ihsv,cv2.COLOR_HSV2BGR)
cv2.imshow('Anh nguoc', img_hsv_bgr)

#Cach khac:
Iv_new = np.zeros((h, w, 3), dtype='uint8')
gamma = 0.5
Iv_new = hieuchinh_gamma(Ihsv[:,:,2], gamma)
cv2.imshow('Gama', Iv_new)
I4 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow("Anh mau RGB", I4)

if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
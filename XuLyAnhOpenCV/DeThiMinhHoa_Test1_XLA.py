import cv2
from PIL import Image
# Câu 1 (2 điểm). Hiển thị ảnh, hiển thị kênh R của ảnh I. 
I=cv2.imread("CMND01_300_500.png")
print('# Cau 1 (2 điểm). Hiển thị ảnh')
cv2.imshow('Colors',I)

R=I[:,:,2]
print(', hiển thị kênh R của ảnh I. ')
cv2.imshow('Cau1: Anh kenh R',R)

# Câu 2 (3 điểm). Chuyển ảnh sang ảnh grayscale được ảnh Ig mà không dùng hàm thư viện của OpenCV và hiển thị ảnh Ig.

B, G, R = I[:,:,0], I[:,:,1], I[:,:,2]
Ig = 0.2989 * R + 0.5870 * G + 0.1140 * B
print('# Cau 2 (3 điểm). Chuyển ảnh sang ảnh grayscale được ảnh Ig mà không dùng hàm thư viện của OpenCV và hiển thị ảnh Ig.')
cv2.imshow('Cau 2: Anh Ig',Ig)

#Cach khac:
img_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
cv2.imshow("img gray", img_gray)
h, w, d = I.shape

def bgr2gray(I):
    for i in range(h):
        for j in range(w):
            px = I[i][j]
            avg = (np.uint8(np.average(px)))
            I[i][j] = [avg, avg, avg]
    return I
    Ig = bgr2gray(I)
    cv2.imshow("Gray", Ig)


# Câu 3 (2 điểm). Chuyển ảnh Ig sang ảnh nhị phân Ib với ngưỡng quyết định nhị phân 90. Hiển thị ảnh nhị phân Ib.
Nguong_thresh_hold,I_threshold=cv2.threshold(Ig, 90, 255, cv2.THRESH_BINARY)
print('# Cau 3 (2 điểm). Chuyển ảnh Ig sang ảnh nhị phân Ib với ngưỡng quyết định nhị phân 90. Hiển thị ảnh nhị phân Ib.')
cv2.imshow('Cau 3: Nguong nhi phan Ib',I_threshold)

# Câu 4 (1 điểm). Làm trơn ảnh Ig theo bộ lọc median với lân cận cửa sổ kích thước 5x5 thu được ảnh Im. Hiển thị ảnh kết quả Im.
import numpy as np
Ir,Ig,Ib=cv2.split(I)
h=I.shape[0]
w=I.shape[1]
I_m=np.zeros((h,w,5),dtype='uint8')
I_m=cv2.medianBlur(Ig,5)
cv2.imshow('Cau 4: Bộ lọc Median', I_m)

I_m2=cv2.medianBlur(Ig,5)
print('#Câu 4 (1 điểm). Làm trơn ảnh Ig theo bộ lọc median với lân cận cửa sổ kích thước 5x5 thu được ảnh Im. Hiển thị ảnh kết quả Im.')
cv2.imshow('Cau 4: Im', I_m2)

# Câu 5 (1 điểm). Xác định ảnh biên Ie của ảnh Im sử dụng phương pháp Sobel. Hiển thị ảnh kết quả Ie.
#tim bien sobel dao ham theo x
sobelx = cv2.Sobel(I_m, ddepth=cv2.CV_64F, dx = 1, dy = 0, ksize = 5)
#tim bien sobel dao ham theo y
sobely = cv2.Sobel(I_m, cv2.CV_64F, 0, 1, ksize = 5)
cv2.imshow('Cau 5: Sobel x: ', sobelx)
cv2.imshow('Cau 5: Sobel y: ', sobely)
print('# Cau 5 (1 điểm). Xác định ảnh biên Ie của ảnh Im sử dụng phương pháp Sobel. Hiển thị ảnh kết quả Ie.')

# Câu 6 (1 điểm). Xác định các contour của ảnh Im và vẽ vị trí các contour lên ảnh gốc I ban đầu.
ret, thress = cv2.threshold(Ig, 127, 255, 0)
contours, hierarchy = cv2.findContours(thress, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #tim contour
#ve lai anh contour vao anh goc
img_draw = cv2.drawContours(I, contours, -1, (0,255,0), 3)
cv2.imshow("Cau 6: Img draw", img_draw)
print('# Cau 6 (1 điểm). Xác định các contour của ảnh Im và vẽ vị trí các contour lên ảnh gốc I ban đầu.')
if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
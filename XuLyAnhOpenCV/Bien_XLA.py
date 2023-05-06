import cv2
import numpy as np
I = cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\Coins.jpg')
cv2.imshow('Colors',I)

Igray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) 
cv2.imshow('Gray',Igray)

# mình muốn lấy ảnh đồng xu thì dùng blur 
I = cv2.blur(Igray,(3,3)) #lọc ảnh trung bình của sổ lọc 3x3
#Tìm biên theo SOBEL
sobelx = cv2.Sobel(I,ddepth=cv2.CV_64F, dx=1, dy=0, ksize=1)  # tìm biên sobel đạo hàm theo x tham số của thuật toán bt là đc
sobely = cv2.Sobel(I,cv2.CV_64F,0,1,ksize=1)  #  tìm biên sobel đạo hàm the y
# sau khi tìm đc sobel x vs sobel y thì hiển thị ảnh là lấy các viền khác nhau
# tìm xong phải in ra
cv2.imshow('Sobel x: ', sobelx)
cv2.imshow('Sobel y: ', sobely)
img = cv2.GaussianBlur(Igray,(3,3),0) #lọc ảnh Gaussian 

# tìm biên là phải blur trc
img = cv2.GaussianBlur(Igray,(3,3),0) #lọc ảnh Gaussian 

#Tìm biên theo Laplacian và Canny 
laplacian = cv2.Laplacian(img,cv2.CV_64F) #tìm biên theo laplacian
cv2.imshow('Laplacian', laplacian)
Icanny = cv2.Canny(image=I, threshold1=100, threshold2=200) # tìm biên theo Canny 
cv2.imshow('Icanny', Icanny)

# Lấy biên Sobel trung bình theo cả x và y --------------
img_gaussian = cv2.GaussianBlur(Igray,(5,5),0)
 
img_sobelx = cv2.Sobel(img_gaussian,ddepth=cv2.CV_64F, dx=1, dy=0, ksize=1)  # tìm biên sobel đạo hàm theo x
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_64F,0,1,ksize=1)  #  tìm biên sobel đạo hàm the y

img_sobelx = np.uint8(np.absolute(img_sobelx))
img_sobely = np.uint8(np.absolute(img_sobely))

img_sobel = (img_sobelx + img_sobely)/2 #vì sobel chỉ lấy cả x vs y nên phải tính tb
for i in range(img_sobel.shape[0]):
    for j in range(img_sobel.shape[1]):
        if img_sobel[i][j] < 25:
            img_sobel[i][j] = 0
        else:
            img_sobel[i][j] = 255

cv2.imshow('Sobel x', img_sobelx)
cv2.imshow('Sobel y', img_sobely)
# ảnh in ra lấy ra theo sobel tb
cv2.imshow('Sobel', img_sobel)

#C1: Theo ngưỡng nhị phân
thresh, I_bina = cv2.threshold(Igray, 80, 255, cv2.THRESH_BINARY)#nhij phaan anhr cangf nets thif timf bieen trong contour cangf rox
cv2.imshow('Binnary gray',I_bina)

#copy từ ảnh gốc để đổi đc màu biên
I_copy = I.copy() 
contours, hierarchy = cv2.findContours(I_bina, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#lệnh tìm đường viền gồm có ảnh muốn tìm - chế độ tìm - phương pháp tìm
cv2.drawContours(I_copy   , contours, -1, (0,255,0), 3) #tìm được rồi thì ta sẽ vẽ đường viền đó vào trong ảnh, vẽ trên ảnh gốc thay đổi 0 255 để thay đổi màu biên

# vì trong contour còn có contour khác nên ta phải xét từng contour để lọc
for contour in contours:
  if cv2.contourArea(contour) > 200: #mình thay đổi 200 ở đây để lọc contour
      cv2.drawContours(I_copy, [contour], -1, (0,255,0), 3)
cv2.imshow('Copy', I_copy)

#C2: Theo ngưỡngTHRESH_OTSU / ADAPTIVE_THRESH_GAUSSIAN_C / ADAPTIVE_THRESH_MEAN_C
thresh, Ib = cv2.threshold(Igray, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('Otsu', Ib)

thresh, I_binary=cv2.threshold(Igray,90,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
cv2.imshow('Gaussian', I_binary)

thresh, I_binary=cv2.threshold(Igray,90,255, cv2.ADAPTIVE_THRESH_MEAN_C)
cv2.imshow('Adaptive', I_binary)

#5. Loại bỏ các contour bé
for contour in contours:
#chỉnh 200 để lấy đầy đủ ảnh 
  if cv2.contourArea(contour) > 200:
      cv2.drawContours(I_copy, [contour], -1, (0,255,0), 3)
cv2.imshow('Chinh anh',I_copy)

if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
import cv2
import numpy as np

# Đọc và hiển thị ảnh Coins.jpg 
# I = cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\Coins.jpg')
I = cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\Tao.jpg')
cv2.imshow('Colors',I)

#Chuyển ảnh I thành ảnh grayscale I_gray
Igray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) 
cv2.imshow('Gray',Igray)

#Chuyển từ ảnh Igray sang ảnh nhị phân I_bina
#C1: Theo ngưỡng nhị phân
thresh, I_bina = cv2.threshold(Igray, 90, 255, cv2.THRESH_BINARY)
cv2.imshow('Anh nhi phan nguong 90', I_bina)

#Tự viết hàm nhị phân ảnh
def change_image(I,thresh):
   h,w = I.shape
   Ib = np.zeros((h,w))
   for t in range(h):
    for t1 in range(w):
       if I[t][t1] < thresh:
           Ib[t][t1]=0
       else: Ib[t][t1] = 255
    return Ib
I_bina = change_image(Igray,120)
cv2.imshow('Anh nhi phan',I_bina)

#C2: Theo ngưỡngTHRESH_OTSU / ADAPTIVE_THRESH_GAUSSIAN_C / ADAPTIVE_THRESH_MEAN_C
Igray = cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)
ret, img_binary = cv2.threshold(Igray, 90, 255, cv2.THRESH_OTSU)

thresh, I_binary=cv2.threshold(Igray,90,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
cv2.imshow('Anh nhi phan Gaussian',I_binary)

thresh, I_binary=cv2.threshold(Igray,90,255, cv2.ADAPTIVE_THRESH_MEAN_C)
cv2.imshow('Anh nhi phan Adaptive',I_binary)

#4. Tìm  contour của ảnh I_bina
#copy từ ảnh gốc để đổi đc màu biên
I_copy = I.copy()
contours, hierarchy = cv2.findContours(I_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I_copy, contours, -1, (0,255,0), 3) #vẽ trên ảnh gốc

#5. Loại bỏ các contour bé
#C1:
# vì trong contour còn có contour khác nên ta phải xét từng contour để lọc
for contour in contours:
    #chỉnh 200 để lấy đầy đủ ảnh 
  if cv2.contourArea(contour) > 200:    #mình thay đổi 200 ở đây để lọc contour
      cv2.drawContours(I_copy, [contour], -1, (0,255,0), 3)
cv2.imshow('Contours',I_copy)
#C2: 
Icc = I.copy()
max_area=0.0
for cnt in contours:
    if max_area < cv2.contourArea(cnt):
        max_area=cv2.contourArea(cnt)
for cnt in contours:
    if cv2.contourArea(cnt) > max_area/2:
        cv2.drawContours(Icc,[cnt],-1,(0,0,255),2)
cv2.imshow("Bo cac contour qua nho",Icc)

#6. Đổi ảnh tao.jpg --> nhận xét: không tìm được contour chính xác --> giải pháp 
#B1: Đổi ảnh nền trắng sang ảnh nền đen 
I_binary = 255 - I_binary
#B2: Chỉnh ngưỡng chuyển ảnh nhị phân
thresh, Ib = cv2.threshold(Igray, 180, 255, cv2.THRESH_BINARY)

#Loc anh trung binh
Igray1 = cv2.blur(Igray,(3,3)) #lọc ảnh trung bình
#Tìm biên theo SOBEL
sobelx = cv2.Sobel(Igray1,ddepth=cv2.CV_64F, dx=1, dy=0, ksize=1)  # tìm biên sobel đạo hàm theo x
sobely = cv2.Sobel(Igray1,cv2.CV_64F,0,1,ksize=1)  #  tìm biên sobel đạo hàm the y
cv2.imshow('Sobel x', sobelx)
cv2.imshow('Sobel y', sobely)

#Tìm biên theo Laplacian và Canny 
Igray2 = cv2.GaussianBlur(Igray,(3,3),0) #lọc ảnh Gaussian 
laplacian = cv2.Laplacian(Igray2,cv2.CV_64F) #tìm biên theo laplacian
Icanny = cv2.Canny(image=Igray2, threshold1=100, threshold2=200) # tìm biên theo Canny 
cv2.imshow('Laplacian', laplacian)
cv2.imshow('Icanny', Icanny)

# Lấy biên Sobel trung bình theo cả x và y --------------
img_gaussian = cv2.GaussianBlur(Igray,(5,5),0)
 
img_sobelx = cv2.Sobel(img_gaussian,ddepth=cv2.CV_64F, dx=1, dy=0, ksize=1)  # tìm biên sobel đạo hàm theo x
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_64F,0,1,ksize=1)  #  tìm biên sobel đạo hàm the y

img_sobelx = np.uint8(np.absolute(img_sobelx))
img_sobely = np.uint8(np.absolute(img_sobely))

img_sobel = (img_sobelx + img_sobely)/2
for i in range(img_sobel.shape[0]):
    for j in range(img_sobel.shape[1]):
        if img_sobel[i][j] < 25:
            img_sobel[i][j] = 0
        else:
            img_sobel[i][j] = 255

cv2.imshow('Img sobel x', img_sobelx)
cv2.imshow('Img sobel y', img_sobely)
cv2.imshow('Sobel', img_sobel)

#C1: Theo ngưỡng nhị phân
thresh, I_bina = cv2.threshold(Igray1, 90, 255, cv2.THRESH_BINARY)
cv2.imshow('Nhi phan', I_bina)

I_copy = I.copy()
contours, hierarchy = cv2.findContours(I_bina, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  #lệnh tìm đường viền gồm có ảnh muốn tìm - chế độ tìm - phương pháp tìm
cv2.drawContours(I_copy   , contours, -1, (255,0,0), 3) #tìm được rồi thì ta sẽ vẽ đường viền đó vào trong ảnh, vẽ trên ảnh gốc thay đổi 0 255 để thay đổi màu biên
cv2.imshow('Copy', I_copy)

for contour in contours:
  if cv2.contourArea(contour) > 1000:
      cv2.drawContours(I_copy, [contour], -1, (0,255,0), 3)
cv2.imshow('Copy contours', I_copy)

#C2: Theo ngưỡngTHRESH_OTSU / ADAPTIVE_THRESH_GAUSSIAN_C / ADAPTIVE_THRESH_MEAN_C
thresh, Ib = cv2.threshold(Igray, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('Nhi phan Gray', Ib)

thresh, I_binary=cv2.threshold(Igray,90,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
cv2.imshow('Gaussian', I_binary)

thresh, I_binary=cv2.threshold(Igray,90,255, cv2.ADAPTIVE_THRESH_MEAN_C)
cv2.imshow('Adaptive', I_binary)

if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
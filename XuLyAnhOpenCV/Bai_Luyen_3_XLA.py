import cv2
import matplotlib.pyplot as plt

# Đọc ảnh mầu I04.jpg vào biến ma trận I.
# 1.  Hiển thị  ảnh I 
I = cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\I04.jpg')
cv2.imshow('Colors', I)

# 2. Chỉnh size mới cho ảnh là độ cao 256, ảnh giữ nguyên tỷ lệ so với ảnh gốc, được ảnh mới I2. Hiển thị ảnh I2.
(h, w, c) = I.shape
I2= cv2.resize(I,(h,256))
cv2.imshow('I2', I2)

#3. Chuyển đổi ảnh I sang ảnh HSV được ma trận ảnh Ihsv. Hiển thị kênh V của ảnh Ihsv.
img_hsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
H,S,V=cv2.split(img_hsv)
cv2.imshow('Kênh V', V)

#4. Làm trơn ảnh I trên từng kênh theo phương pháp Gaussain. Hiển thị ảnh I 
B,G,R=cv2.split(I)
img_gsB=cv2.GaussianBlur(B,(3,3),0)
img_gsG=cv2.GaussianBlur(G,(3,3),1)
img_gsR=cv2.GaussianBlur(R,(3,3),2)
cv2.imshow('Kênh B', B)
cv2.imshow('Kênh G',G)
cv2.imshow('Kênh R',R)
cv2.imshow('Img Kênh B', img_gsB)
cv2.imshow('Img Kênh G', img_gsG)
cv2.imshow('Img Kênh R', img_gsR)

#5. Cân bằng histogram của  kênh V của ảnh Ihsv. Hiển thị ảnh Ihsv, so sánh với câu 3. Biến đổi ngược ảnh Ihsv về biểu diễn mầu RGB được ảnh I4. Hiển thị ảnh I4.
#Cach 1:
hV_equal=cv2.equalizeHist(V)
cv2.imshow('Anh kenh V CBang', hV_equal)
img_hsv_bgr=cv2.cvtColor(img_hsv,cv2.COLOR_HSV2BGR)
cv2.imshow('Bien doi nguoc', img_hsv_bgr)

#Cach 2:
Ihsv_2 = cv2.equalizeHist(V)
cv2.imshow("Anh kenh V CB ",Ihsv_2)
#Vẽ histogram của kênh V của ảnh Ihsv sau khi cân bằng.
Hist_V=cv2.calcHist([Ihsv_2],[0],None,[256],[0,256])
plt.title("Cân bằng Histogram kênh V (❁´◡`❁)")
plt.plot(Hist_V,color="Black") #=)))) thay thành màu nào thích là được
plt.show()
# Biến đổi ngược ảnh Ihsv về biểu diễn mầu RGB được ảnh I4. Hiển thị ảnh I4.
I4 = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("BGR", I4)

if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
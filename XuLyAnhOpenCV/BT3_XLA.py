import cv2

#Doc Anh
I = cv2.imread('G:\XuLyAnhOpenCV\ThoNgoc.jpg')
cv2.imshow('Original image', I)

#2. Chuyển ảnh màu thành ảnh xám
I_gray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) 
cv2.imshow('Color image',I_gray)

#Chuyển từ ảnh xám sang ảnh trắng đen với ngưỡng 90
I_baclkwhite, threshold = cv2.threshold(I_gray, 90, 255, cv2.THRESH_BINARY)
cv2.imshow('Color binary',threshold)

#Chuyển từ ảnh xám sang ảnh trắng đen theo ngưỡng OTSU 
I_baclkwhite, threshold = cv2.threshold(I_gray,125,255,cv2.THRESH_OTSU)
cv2.imshow('Color otsu',threshold)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh và chuyển sang ảnh xám
I = cv2.imread(path)
I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Nhị phân hóa ảnh theo ngưỡng Otsu
_, I_bina = cv2.threshold(I_gray, 0, 255, cv2.THRESH_OTSU)

# Tìm các contours trong ảnh
contours, hierarchy = cv2.findContours(I_bina, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Vẽ các contours lên ảnh gốc
cv2.drawContours(I, contours, -1, (0, 0, 255), 2)

# Hiển thị ảnh
cv2.imshow('Contours', I)
cv2.waitKey(0)

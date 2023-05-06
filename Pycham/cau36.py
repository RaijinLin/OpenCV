import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'



# Load ảnh gốc
I = cv2.imread(path)

# Chuyển sang ảnh grayscale
I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Áp dụng phương pháp Otsu để nhị phân ảnh
thresh, I_bina = cv2.threshold(I_gray, 0, 255, cv2.THRESH_OTSU)

# Tìm các đường contour
contours, hierarchy = cv2.findContours(I_bina, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Tìm contour có diện tích lớn nhất
max_area = 0
max_contour = None
for contour in contours:
    area = cv2.contourArea(contour)
    if area > max_area:
        max_area = area
        max_contour = contour

# Vẽ contour lớn nhất lên ảnh gốc
cv2.drawContours(I, [max_contour], 0, (0, 255, 0), 3)

# Hiển thị ảnh gốc với contour lớn nhất
cv2.imshow('Largest Contour', I)
cv2.waitKey(0)
cv2.destroyAllWindows()

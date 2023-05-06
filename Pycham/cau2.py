import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'
# Đọc ảnh Igray
Igray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Áp dụng phương pháp ngưỡng Otsu
ret, Ib = cv2.threshold(Igray, 0, 255, cv2.THRESH_OTSU)

# Hiển thị ảnh nhị phân Ib
cv2.imshow("anh nhi phan theo otsu", Ib)
cv2.waitKey()
cv2.destroyAllWindows()
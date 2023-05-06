import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh vào
img = cv2.imread(path)

# Chuyển sang ảnh đa cấp xám
h, w, k = img.shape
Igray = np.zeros((h, w), dtype='uint8')
b, g, r = cv2.split(img)
Igray[:, :] = 0.39 * r + 0.5 * g + 0.11 * b

# Hiển thị ảnh Ig
cv2.imshow('Igray', Igray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Chuyển sang ảnh nhị phân Ib với ngưỡng Otsu
ret, Ib = cv2.threshold(Igray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Hiển thị ảnh Ib
cv2.imshow('Ib', Ib)
cv2.waitKey(0)
cv2.destroyAllWindows()


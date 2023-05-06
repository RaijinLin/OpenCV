import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh vào
I = cv2.imread(path)

# Chuyển đổi sang biểu diễn HSV
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)

# Hiển thị kênh V của Ihsv
cv2.imshow('Kenh V', Ihsv[:, :, 2])
cv2.waitKey(0)

# Tìm giá trị mức sáng lớn nhất và nhỏ nhất của kênh S
max_s = np.max(Ihsv[:, :, 1])
min_s = np.min(Ihsv[:, :, 1])
print('Gia tri muc sang lon nhat cua kenh S:', max_s)
print('Gia tri muc sang nho nhat cua kenh S:', min_s)

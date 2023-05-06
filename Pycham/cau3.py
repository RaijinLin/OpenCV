import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh màu
img = cv2.imread(path)

# Lấy chiều rộng, chiều cao và số kênh màu của ảnh
h, w, k = img.shape

# Khởi tạo ma trận ảnh xám
Igray = np.zeros((h, w), dtype='uint8')

# Tách kênh màu
b, g, r = cv2.split(img)

# Tính toán mức độ xám cho từng pixel và gán vào ma trận ảnh xám
Igray[:, :] = 0.39 * r + 0.5 * g + 0.11 * b

# Hiển thị ảnh xám
cv2.imshow('Grayscale Image', Igray)
cv2.waitKey(0)
cv2.destroyAllWindows()

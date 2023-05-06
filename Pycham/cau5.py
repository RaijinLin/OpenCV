import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh đầu vào
img = cv2.imread(path)

# Chuyển đổi sang ảnh xám
h,w,k = img.shape
Igray = np.zeros((h, w), dtype='uint8')
b,g,r = cv2.split(img)
Igray[:, :] = 0.39 * r + 0.5 * g + 0.11 * b

# Hiển thị ảnh Igray
cv2.imshow('Grayscale Image', Igray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Tìm mức xám lớn nhất của ảnh Igray
max_gray_level = np.max(Igray)
print('Mức xám lớn nhất của ảnh Igray:', max_gray_level)

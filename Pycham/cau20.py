import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Load ảnh I
I = cv2.imread(path)

# Lấy kích thước của ảnh
height, width, channels = I.shape

# Tính tỷ lệ giữa chiều cao mới và chiều cao của ảnh gốc
new_height = 256
aspect_ratio = new_height / float(height)

# Tính chiều rộng mới
new_width = int(width * aspect_ratio)

# Thay đổi kích thước ảnh
resized_img = cv2.resize(I, (new_width, new_height))

# Hiển thị ảnh mới lên màn hình
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

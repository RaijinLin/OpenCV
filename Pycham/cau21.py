import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh I vào biến img
img = cv2.imread(path)

# Lấy chiều cao và chiều rộng của ảnh
h, w = img.shape[:2]

# Tính tỉ lệ giữa chiều cao và chiều rộng của ảnh
ratio = float(h) / float(w)

# Xác định kích thước mới cho ảnh
new_size = (256, int(256 * ratio))

# Thay đổi kích thước của ảnh
resized_img = cv2.resize(img, new_size, interpolation=cv2.INTER_AREA)

# Tạo một mảng trống có kích thước mới là (256, 256)
delta_w = 256 - new_size[1]
delta_h = 256 - new_size[0]

if delta_h < 0 or delta_w < 0:
    resized_img = cv2.copyMakeBorder(resized_img, abs(delta_h)//2, abs(delta_h)//2 + abs(delta_h)%2, abs(delta_w)//2, abs(delta_w)//2 + abs(delta_w)%2, cv2.BORDER_CONSTANT, value=(0, 0, 0))
else:
    resized_img = np.array(resized_img)

# Hiển thị ảnh mới
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

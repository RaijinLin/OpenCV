import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Load ảnh
img = cv2.imread(path)

# Chuyển đổi ảnh từ không gian màu RGB sang không gian màu HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Tách kênh V của ảnh
v_channel = hsv[:, :, 2]

# Áp dụng bộ lọc Gaussian để làm mờ kênh V
v_blur = cv2.GaussianBlur(v_channel, (5, 5), 0)

# Sử dụng phương pháp Canny để xác định biên của kênh V
v_canny = cv2.Canny(v_blur, 100, 200)

# Chuyển đổi ảnh nhị phân được thành ảnh nhị phân Ivb
ivb = np.zeros_like(v_canny)
ivb[v_canny > 0] = 255

# Hiển thị ảnh Ivb
cv2.imshow('anh-goc', img)
cv2.imshow('Ivb', ivb)
cv2.waitKey(0)
cv2.destroyAllWindows()

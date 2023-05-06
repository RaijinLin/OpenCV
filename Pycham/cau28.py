import cv2
import numpy as np
path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh và chuyển sang không gian màu HSV
img = cv2.imread(path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Lấy kênh V của không gian màu HSV
v_channel = hsv[:, :, 2]

# Làm trơn ảnh kênh V bằng bộ lọc trung bình cộng 3x3
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
v_blur = cv2.blur(v_channel, (3, 3))

# Hiển thị ảnh Iv sau khi làm trơn
cv2.imshow('Iv', v_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

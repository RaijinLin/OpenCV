import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh và chuyển sang không gian màu HSV
img = cv2.imread(path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Lấy kênh S của không gian màu HSV
s_channel = hsv[:, :, 1]

# Làm trơn ảnh kênh S bằng bộ lọc median 3x3
s_blur = cv2.medianBlur(s_channel, 3)

# Biến đổi ngược ảnh Ihsv về không gian màu RGB
hsv[:, :, 1] = s_blur
rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

# Hiển thị ảnh I sau khi biến đổi ngược
cv2.imshow('I', rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

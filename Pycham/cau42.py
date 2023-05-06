import cv2
import numpy as np
path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh ban đầu
img = cv2.imread(path)

# Chuyển đổi sang không gian màu HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Tách kênh V của ảnh
v_channel = hsv_img[:,:,2]

# Giãn mức xám trên kênh V
v_min = np.min(v_channel)
v_max = np.max(v_channel)
v_new = ((v_channel - v_min) * 255) / (v_max - v_min)

# Ghép kênh V mới vào ảnh ban đầu
hsv_img[:,:,2] = v_new

# Biến đổi ảnh Ihsv về biểu diễn mầu RGB
new_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

# Hiển thị ảnh gốc và ảnh sau khi tăng độ sáng kênh V bằng giãn mức xám
cv2.imshow("Original Image", img)
cv2.imshow("New Image", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

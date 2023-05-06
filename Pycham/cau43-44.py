import cv2
import numpy as np
path = r'C:\Users\Hungd\Downloads\rgb.jpg'

# Đọc ảnh và chuyển sang không gian màu HSV
img = cv2.imread(path)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Lấy kênh V của ảnh
v_channel = hsv[:,:,2]

# Tính phạm vi giá trị mức xám ban đầu và kết quả mong muốn
v_min = np.min(v_channel)
v_max = np.max(v_channel)
v_new_min = 0
v_new_max = 255

# Tính hằng số a và b
a = (v_new_max - v_new_min) / (v_max - v_min)
b = v_new_min - a * v_min

# Tăng độ sáng kênh V bằng phương pháp giãn tuyến tính các giá trị mức xám
v_new = np.clip(a * v_channel + b, 0, 255).astype(np.uint8)

# Gán kênh V mới vào ảnh HSV
hsv[:,:,2] = v_new

# Chuyển về không gian màu RGB
rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Hiển thị ảnh
cv2.imshow('anhgoc', img)
cv2.imshow('Image', rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

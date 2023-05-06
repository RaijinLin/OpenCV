import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh đầu vào
img = cv2.imread(path)

# Chuyển đổi sang không gian màu HSV
Ihsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Hiển thị kênh S
cv2.imshow('S Channel', Ihsv[:, :, 1])
cv2.waitKey(0)
cv2.destroyAllWindows()

# Hiển thị các giá trị điểm ảnh trong cửa sổ lân cận 5x5 tại tọa độ dòng y=10, cột x=20
print(Ihsv[8:13, 18:23])

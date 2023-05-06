import cv2
import numpy as np
path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh Ig
img = cv2.imread(path, 0)

# Lấy biên ảnh Ig theo phương pháp Canny
edges = cv2.Canny(image=img, threshold1=100, threshold2=200)

# Hiển thị ảnh biên Ie
cv2.imshow('Ie', edges)

# Kiểm tra xem điểm có tọa độ dòng y=109, cột x=130 có phải là điểm biên hay không
y = 109
x = 130
if edges[y, x] == 255:
    print('Pixel at (', x, ',', y, ') is an edge.')
else:
    print('Pixel at (', x, ',', y, ') is not an edge.')

cv2.waitKey(0)
cv2.destroyAllWindows()

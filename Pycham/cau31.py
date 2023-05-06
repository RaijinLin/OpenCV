import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh Ig
Ig = cv2.imread(path, 0)

# Lấy biên theo phương pháp Canny
Ie = cv2.Canny(image=Ig, threshold1=100, threshold2=200)

# Hiển thị ảnh Ie
cv2.imshow('Ie', Ie)

# Kiểm tra điểm ảnh tại tọa độ y=100, x=120 có phải là điểm biên hay không
if Ie[100, 200] == 255:
    print("Điểm ảnh này là điểm biên của ảnh Ig theo phương pháp Canny")
else:
    print("Điểm ảnh này không phải là điểm biên của ảnh Ig theo phương pháp Canny")

# Hiển thị ảnh Ig và đợi người dùng nhấn phím bất kỳ để thoát chương trình
cv2.imshow('Ig', Ig)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh gốc
I = cv2.imread(path)

# Chuyển đổi sang ảnh xám và nghịch đảo
I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
Is = cv2.bitwise_not(I_gray)

# Nhị phân hóa ảnh nghịch đảo theo ngưỡng Otsu
thresh, Ib = cv2.threshold(Is, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Tìm các đường contour và diện tích tương ứng
contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
area_cnt = [cv2.contourArea(cnt) for cnt in contours]

# Tìm contour có chu vi lớn nhất
max_perimeter = 0
max_perimeter_idx = 0
for i in range(len(contours)):
    perimeter = cv2.arcLength(contours[i], True)
    if perimeter > max_perimeter:
        max_perimeter = perimeter
        max_perimeter_idx = i

# Vẽ contour tìm được trên ảnh gốc
cv2.drawContours(I, contours, max_perimeter_idx, (0, 0, 255), 3)

# Hiển thị kết quả
cv2.imshow('Result', I)
cv2.waitKey(0)
cv2.destroyAllWindows()

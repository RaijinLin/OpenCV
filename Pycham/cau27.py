import cv2
import numpy as np
path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh và chuyển đổi sang ảnh mức xám
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('anhxam', gray)
if cv2.waitKey() == ord('x'):
    cv2.destroyAllWindows()

    
# Tọa độ điểm ảnh cần tìm lân cận 5x5
y = 9
x = 11

# Trích xuất lân cận 5x5 của điểm ảnh
neighborhood = gray[y-2:y+3, x-2:x+3]

# In ra các giá trị mức xám trong lân cận 5x5
print(neighborhood)

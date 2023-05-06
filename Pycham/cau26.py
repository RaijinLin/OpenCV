import cv2
import numpy as np
path = r'C:\Users\Hungd\Downloads\meo.jpg'

I = cv2.imread(path)

# Chuyển ảnh sang không gian màu HSV
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)

# Trích xuất kênh S của Ihsv
Is = Ihsv[:,:,1]

# Lọc median với kernel có kích thước 5x5
Is_smoothed = cv2.medianBlur(Is, 5)

# Hiển thị ảnh Is sau khi lọc
cv2.imshow("Is_smoothed", Is_smoothed)

if cv2.waitKey() == ord('s'):
    cv2.destroyAllWindows()
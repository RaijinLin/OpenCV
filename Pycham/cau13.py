import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

I = cv2.imread(path)

# Chuyển ảnh sang biểu diễn HSV
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)

# Lấy kênh S của Ihsv
S = Ihsv[:, :, 1]

# Chuyển kênh S sang ảnh nhị phân Ib với ngưỡng Otsu
_, Ib = cv2.threshold(S, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Hiển thị ảnh nhị phân Ib và ảnh gốc I
cv2.imshow("Ib", Ib)
cv2.imshow("I", I)

if cv2.waitKey() == ord('s'):
    cv2.destroyAllWindows()
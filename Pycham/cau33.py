import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

I = cv2.imread(path)

# chuyển đổi ảnh sang grayscale
Igray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# sử dụng phương pháp Otsu để chọn ngưỡng phù hợp
ret, Ib = cv2.threshold(Igray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# hiển thị ảnh kết quả
cv2.imshow('Ib', Ib)

if cv2.waitKey() & 0xff == 27:
    cv2.destroyAllWindows()

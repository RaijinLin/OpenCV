import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

img = cv2.imread(path)


# Chuyển ảnh sang biểu diễn HSV
Ihsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Hiển thị kênh H của Ihsv
cv2.imshow('H Channel', Ihsv[:,:,0])
cv2.waitKey(0)
cv2.destroyAllWindows()

# Xác định giá trị mức sáng lớn nhất của kênh S của Ihsv
max_s = np.max(Ihsv[:,:,1])
print('Max value of S channel:', max_s)

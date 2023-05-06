import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# đọc ảnh gốc
img = cv2.imread(path)

# chuyển đổi không gian màu từ RGB sang HLS
hls_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

# lấy kênh S của ảnh
s_channel = hls_img[:,:,2]

# áp dụng bộ lọc trung bình cộng với lân cận cửa sổ kích thước 5x5
kernel = np.ones((5,5),np.float32)/25
smoothed_s = cv2.filter2D(s_channel, -1, kernel)

# hiển thị ảnh kết quả
cv2.imshow('Smoothed S Channel', smoothed_s)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Đọc ảnh
I = cv2.imread(path)

# Chuyển đổi sang không gian màu HSV
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)

# Tính histogram kênh V
hist, bins = np.histogram(Ihsv[:, :, 2].ravel(), 256, [0, 256])

# Tính tổng số pixel
pixels = np.sum(hist)

# Tính tỉ lệ tích lũy
cumulative = np.cumsum(hist) / pixels

# Tìm giá trị đầu tiên trong tỉ lệ tích lũy > 0.05
alpha = np.argmax(cumulative > 0.05)

# Tạo ảnh mask để chọn pixel có giá trị kênh V > alpha
mask = cv2.threshold(Ihsv[:, :, 2], alpha, 255, cv2.THRESH_BINARY)[1]

# Cân bằng histogram kênh V
Ihsv[:, :, 2] = cv2.equalizeHist(Ihsv[:, :, 2])

# Biến đổi ngược sang không gian màu RGB
Ienhanced = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)

# Hiển thị ảnh gốc và ảnh tăng độ sáng
cv2.imshow("Original", I)
cv2.imshow("Enhanced", Ienhanced)

# Chờ nhấn phím bất kỳ để thoát
cv2.waitKey(0)
cv2.destroyAllWindows()

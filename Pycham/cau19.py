import cv2

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Load ảnh I
I = cv2.imread(path)

# Lấy kích thước của ảnh
height, width, channels = I.shape

# Tính tỷ lệ giữa giá trị độ cao và độ rộng của ảnh
aspect_ratio = float(height) / width

# Hiển thị tỷ lệ lên màn hình
print("Tỷ lệ giữa giá trị độ cao và độ rộng của ảnh I là: {}".format(aspect_ratio))

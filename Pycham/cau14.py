import cv2

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# đọc ảnh
I = cv2.imread(path)

# hiển thị ảnh
cv2.imshow('image', I)

# tính tỉ lệ giữa độ cao và độ rộng của ảnh
h, w, _ = I.shape
ratio = h / w
print('Tỉ lệ giữa độ cao và độ rộng của ảnh:', ratio)

# đợi và thoát
if cv2.waitKey() == ord('s'):
    cv2.destroyAllWindows()
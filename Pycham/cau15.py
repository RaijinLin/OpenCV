import cv2

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Load ảnh Ig
I = cv2.imread(path)
Ig = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Tọa độ của pixel cần xem cửa sổ lân cận
y = 109
x = 130

# Trích xuất cửa sổ lân cận 5x5 của pixel
neighborhood = Ig[y-2:y+3, x-2:x+3]

# Hiển thị ảnh xám và cửa sổ lân cận
cv2.imshow("Image Gray", Ig)
print("Neighborhood:\n", neighborhood)
cv2.waitKey(0)
cv2.destroyAllWindows()

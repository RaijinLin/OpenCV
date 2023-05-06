import cv2
# + Đọc 1 ảnh vào biến bộ nhớ, hiển thị ảnh
I = cv2.imread('G:\XuLyAnhOpenCV\digital-neon.jpg')

cv2.imshow('Original image',I)
# + Hiển thị giá trị điểm ảnh (pixel) tại vị trí hàng số 50, cột số 100, kênh số 1
print ('Pixel (5,10,1) = ', I[50][100][1])
# height = img.shape[0]
# width = img.shape[1]
# channels = img.shape[2]
height,width,channels = I.shape         #ccao,crong,kenh anh
dimensions = I.shape
size_I = I.size

A= height*width

print ("Diện tích của ảnh: ",A)
# Điểm ảnh tại hàng số 50, cột số 100
print ('Pixel (5,10) = ', I[50][100])
Ir, Ig, Ib = cv2.split(I)

cv2.imshow('Red chanel', Ir)
cv2.imshow('Green chanel', Ig)
cv2.imshow('Blue chanel', Ib)
 
print("Chiều dài : ",height)
print("Chiều rộng : ",width)
print("Số kênh : ",channels)
print("Kích thước ảnh : ",dimensions)
print ("Kích thước của ảnh: ", size_I)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
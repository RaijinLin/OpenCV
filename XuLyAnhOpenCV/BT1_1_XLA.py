import cv2

# đọc và hiển thị ảnh

img = cv2.imread('C:\Users\Lin\Desktop\VM\XuLyAnhOpenCV\digital-neon.jpg')

cv2.imshow('Color image', img)

#1. đưa ra chiều cao, chiều rộng, số kênh
dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

print('Kích thước: ', dimensions)
print('Dài: ', height)
print('Rộng: ', width)
print('Số kênh: ', channels)

# hiển thị giá trị điểm ảnh

print('Điểm ảnh: ', img[100, 50, 1])

# hiển thị thích thước ảnh, số kênh

print('Kích thước ảnh: ', img.shape)

#2. hiển thị ảnh từng kênh
# kênh ảnh 1
cv2.imshow('Kênh 1', img[:, :, 0])

# kênh ảnh 2
cv2.imshow('Kênh 2', img[:, :, 1])

# kênh ảnh 3
cv2.imshow('Kênh 3', img[:, :, 2])

#3. hiện thị size ảnh
print("Size ảnh: ", img.size )

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
import cv2

path = r'C:\Users\Hungd\Downloads\rgb.jpg'



img = cv2.imread(path)

###### - img[y,x] - truy cap den 1 diem anh

# px = img[50 , 230]

# px =  img[50,230] = [100,100,100]
#
# print(px)
#
# cv2.imshow('anhbgr', img)
# cv2.waitKey()


##### - img[y,x, kenh] - 'kenh' = 0 - b, 1 - g, 2 - r -- de tach kenh cua anh
#C1

# b = img[:,:,0]
# r = img[:,:,2]
# g = img[:,:,1]
# cv2.imshow('blue', b)
# cv2.imshow('red',r)
# cv2.imshow('green',g)

#C2

# b, g, r = cv2.split(img)
# cv2.imshow('anh goc', img)
# cv2.imshow('blue', b)
# cv2.imshow('red',r)
# cv2.imshow('green',g)



##### img[y_start:y_end,x_start:x_end] ---- truy cap vung anh

path1 = r'C:\Users\Hungd\Downloads\meo.jpg'

img1 = cv2.imread(path1)
#
# spaceimg = img1[50:330, 480:710]
# img1[50:330, 300:530 ] = spaceimg
# cv2.imshow('img-goc-after', img1 )




##### truy cap tat ca cac thuoc tinh cua anh -- shape(), dtype(), size()


print(img1.shape, img1.size, img1.dtype)

cv2.imshow('anh-meo', img1)


if cv2.waitKey() & 0xff == 27 :
    cv2.destroyAllWindows()
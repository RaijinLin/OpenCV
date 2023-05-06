import cv2

path1 = r'C:\Users\Hungd\Downloads\travel.jpg'
path2 = r'C:\Users\Hungd\Downloads\glym.jpg'

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

# bitwise-and   -theo 0

# dest_and = cv2.bitwise_and(img1, img2, mask=None)
#
# cv2.imshow('travel', img1)
# cv2.imshow('glym', img2)
# cv2.imshow('biswise_and', dest_and)



# bitwise-or    -theo 1

# dest_or = cv2.bitwise_or(img1, img2, mask=None)
#
# cv2.imshow('travel', img1)
# cv2.imshow('glym', img2)
# cv2.imshow('biswise_or', dest_or)


# bitwise-xor    - theo 1 va bang thi ve 0

# dest_xor = cv2.bitwise_xor(img1, img2, mask=None)
#
# cv2.imshow('travel', img1)
# cv2.imshow('glym', img2)
# cv2.imshow('biswise_xor', dest_xor)


# biswise-not     - not 0 thi la 1 , not 1 thi la 0

dest_not = cv2.bitwise_not(img1,  mask=None)

cv2.imshow('travel', img1)

cv2.imshow('biswise_not', dest_not)

if cv2.waitKey(0) & 0xff == 27 :
    cv2.destroyAllWindows()



import cv2
import numpy as np
path = r'C:\Users\Hungd\Downloads\meo.jpg'

# read image
I = cv2.imread(path)
I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# threshold using Otsu's method
ret, Ib = cv2.threshold(I_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# find contours
contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# find contour with largest perimeter
max_perimeter = 0
max_contour = None
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    if perimeter > max_perimeter:
        max_perimeter = perimeter
        max_contour = contour

# draw contour on original image
cv2.drawContours(I, [max_contour], 0, (0, 0, 255), 2)

# show image
cv2.imshow('Image with Contour', I)
cv2.waitKey(0)
cv2.destroyAllWindows()

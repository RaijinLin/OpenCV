import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

Ig = cv2.imread(path, 0)

kernel_averaging_5_5 = np.ones((5, 5), np.float32)/25
Im = cv2.filter2D(Ig, -1, kernel_averaging_5_5)

cv2.imshow("Original Image", Ig)
cv2.imshow("Smoothed Image", Im)

cv2.waitKey(0)
cv2.destroyAllWindows()

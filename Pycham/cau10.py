import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Load the image
img = cv2.imread(path)

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Display the S channel
cv2.imshow('S channel', hsv[:, :, 1])

# Find the maximum value in the V channel
max_v = np.max(hsv[:, :, 2])
print('Max V value:', max_v)

cv2.waitKey(0)
cv2.destroyAllWindows()

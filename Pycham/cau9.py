import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Load the image
I = cv2.imread(path)

# Convert to HSV
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)

# Display the H channel
cv2.imshow('H channel', Ihsv[:, :, 0])

# Calculate the average saturation of the S channel
S_avg = np.mean(Ihsv[:, :, 1])
print('Average S value:', S_avg)

cv2.waitKey(0)
cv2.destroyAllWindows()

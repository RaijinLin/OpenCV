import cv2
import numpy as np
path = r'C:\Users\Hungd\Downloads\meo.jpg'

# Load the input image
I = cv2.imread(path)

# Convert the input image to grayscale
I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Threshold the grayscale input image using Otsu's method
thresh, I_bina = cv2.threshold(I_gray, 0, 255, cv2.THRESH_OTSU)

# Create a copy of the input image
I_copy = I.copy()

# Extract the contours from the binary image
contours, hierarchy = cv2.findContours(I_bina, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Compute the area of each contour
area_cnt = [cv2.contourArea(cnt) for cnt in contours]

# Find the contour with the largest area
max = area_cnt[0]
for i in range(len(area_cnt)):
    if max < area_cnt[i]:
        max = area_cnt[i]

# Draw contours with an area greater than 1/5 of the largest contour area on the input image
for contour in contours:
    if cv2.contourArea(contour) > (max / 5):
        cv2.drawContours(I_copy, [contour], -1, (0, 255, 255), 3)

# Display the resulting image with contours overlaid on the input image
cv2.imshow('Contours', I_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

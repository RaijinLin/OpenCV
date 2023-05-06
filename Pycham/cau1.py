import cv2
import matplotlib.pyplot as plt

path = r'C:\Users\Hungd\Downloads\rgb.jpg'

img = cv2.imread(path)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

S = img_hsv[:,:,1]
S_equalized = cv2.equalizeHist(S)
f, axes = plt.subplots(2, 2, figsize=(30, 20))
axes[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0, 0].set_title('Original Image')
axes[0, 1].imshow(cv2.cvtColor(cv2.merge((img_hsv[:,:,0], S_equalized, img_hsv[:,:,2])), cv2.COLOR_HSV2RGB))
axes[0, 1].set_title('Histogram Equalized Image')
axes[1, 0].hist(S.flatten(), 256, [0, 256])
axes[1, 0].set_title('Original Image Histogram')
axes[1, 1].hist(S_equalized.flatten(), 256, [0, 256])
axes[1, 1].set_title('Histogram Equalized Image Histogram')
plt.show()
plt.close()


import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

img = cv2.imread(path)

Ihsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

H = Ihsv[:, :, 0]
cv2.imshow('kenh H', H)

if cv2.waitKey() == ord('h'):
    cv2.destroyAllWindows()

max_s = np.max(Ihsv[:, :, 1])
print('Gia tri muc sang lon nhat cua kenh S la:', max_s)
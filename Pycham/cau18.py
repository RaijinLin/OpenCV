import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

img = cv2.imread(path)

Ihsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

S = Ihsv[:, :, 1]

cv2.imshow('kenh S', S)

if cv2.waitKey() == ord('s'):
    cv2.destroyAllWindows()

avg_V = np.mean(Ihsv[:,:, 2])
print('Gia tri muc sang tb cua kenh V : ', avg_V)
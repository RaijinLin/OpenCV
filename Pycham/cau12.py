import cv2
import numpy as np

path = r'C:\Users\Hungd\Downloads\meo.jpg'

img = cv2.imread(path)

Ihsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('kenh S', Ihsv[:,:,1])

if cv2.waitKey() == ord('s'):
    cv2.destroyAllWindows()

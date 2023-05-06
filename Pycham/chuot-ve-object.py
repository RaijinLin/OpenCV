import cv2

path = r'C:\Users\Hungd\Downloads\meo.jpg'

def drawCircle(event, x, y, flag, param):
    if(event  == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img, (x,y), 10, (0, 0, 255), 10)

img  = cv2.imread(path)
cv2.namedWindow('anh-meo')
cv2.setMouseCallback('anh-meo', drawCircle)


while(1):
    cv2.imshow('anh-meo', img);

    if cv2.waitKey(100) & 0xff == 27:
      break
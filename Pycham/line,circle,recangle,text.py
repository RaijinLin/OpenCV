import cv2
path = r'C:\Users\Hungd\Downloads\meo.jpg'

img = cv2.imread(path)


##### ve duong thang
'''
start_point = (0, 0)
end_point = (200, 150)
color = (255, 0,0)
thickness = 7
img = cv2.line(img, start_point, end_point, color, thickness)
'''


##### ve duong tron
'''
center = (450, 330)
radious = 300
color = (0, 0, 255)
thickness = 10

img = cv2.circle(img, center, radious, color, thickness)
'''

##### ve hinh chu nhat

'''
start_point = ( 200, 300)
end_point = (700, 500)
color = (0, 255, 0)
thickness = 10

img = cv2.rectangle(img, start_point, end_point, color, thickness)
'''

##### viet text

text = 'hung dz'
org = (260, 400)
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
fontScale = 3

color = (0, 0, 255)
thickness = 5

img = cv2.putText(img,text, org,font, fontScale, color, thickness)

cv2.imshow('anh-meo',img)

if cv2.waitKey() & 0xff == 27 :
    cv2.destroyAllWindows()
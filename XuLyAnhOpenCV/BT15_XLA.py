import cv2
#Doc anh, hien thi anh
I=cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\dark.jpg')
cv2.imshow('Colors',I)

#Hiệu chỉnh Gama khác nhau (0.0 < gama <1.0), chạy code sau và so sánh kết quả. 
import numpy as np
def hieuchinh_gamma(Igray, gamma = 1.0):
  w=Igray.shape[1]
  h=Igray.shape[0]

  Igray_new=np.zeros((h,w),dtype='uint8')
  for i in range(h):
    for j in range(w):
      g_f=float(Igray[i][j])/255.0
      g_f_new=np.power(g_f, gamma)
      g_new=int(g_f_new*255.0)
      Igray_new[i][j]=g_new
  return Igray_new

I=cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\dark.jpg')
cv2.imshow('Colors',I)
Ir=I[:,:,2]
Ig=I[:,:,1]
Ib=I[:,:,0]

w=I.shape[1]
h=I.shape[0]
I_new=np.zeros((h,w,3),dtype='uint8')
gamma=1
cv2.imshow('Anh hieu chinh den',I_new)

I_newgray=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
I_new2=hieuchinh_gamma(I_newgray,gamma)
print('Ảnh bị hiệu chỉnh ánh sáng cho màu đen là:')
cv2.imshow('Anh hieu chinh anh sang mau den',I_new2)

gamma=0.5
I_new3=hieuchinh_gamma(I_new2,gamma)
print('Ảnh sau khi làm sáng lên:')
cv2.imshow('Anh hieu chinh lam sang', I_new3)

if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
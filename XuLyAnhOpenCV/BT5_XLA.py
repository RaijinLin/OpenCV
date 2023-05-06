import cv2

# Bài 5e.Đọc vào ảnh clother1.jpg được ma trận ảnh I.
I = cv2.imread('G:\XuLyAnhOpenCV\minhhoa_anh\clother1.jpg')
cv2.imshow('Colors',I)

# Sử dụng hàm thư viện OpenCV chuyển đổi ảnh I sang biểu diễn mầu HSV được ma trận ảnh Ihsv.
I_HSV = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow('Colors Blue', I_HSV[:,:,0])
cv2.imshow('Colors Green', I_HSV[:,:,1])
cv2.imshow('Colors Red', I_HSV[:,:,2])
cv2.imshow('Colors I_HSV', I_HSV)

I_RBG = cv2.cvtColor(I_HSV, cv2.COLOR_BGR2RGB)
cv2.imshow('Colors I_RGB',I_RBG)

# Hiển thị kênh H. Xác định mức xám trung bình của kênh V.
print('Hiển thị kênh H')
import numpy as np
V,S,H = cv2.split(I_HSV)
print("Giá trị xám của kênh R của I: a = min({}), b = max({})".format(np.min(V),np.max(V)))
minV = np.min(V)
maxV = np.max(V)
MucSangTB = (minV+maxV)//2
print('Gia tri muc sang tb cua V la:',MucSangTB)

# 5g. Không sử dụng hàm thư viện của OpenCV, viết 1 hàm gọi là bgr2hsv chuyển 1 ma trận ảnh I sang ảnh HSV để làm câu 5e.
def ChuyenHSV(I):
  I_HSV = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
  return I_HSV

I_HSV_test=ChuyenHSV(I)
cv2.imshow('Colors I_HSV_Test',I_HSV_test)

# 5h. Gán các giá trị mức xám của kênh V của ảnh Ihsv đều trắng tuyệt đối.
v = I_HSV[:, :, 2]
w = v.shape[1]
h = v.shape[0]
def chuyen(v):
    for i in range(h):
        for j in range(w):
            if v[i][j] != 255:
                v[i][j] = 255
    return v
cv2.imshow('Trắng tuyệt đối', chuyen(v))

# Sử dụng hàm thư viện của OpenCV chuyển đổi ngược Ihsv về biểu diễn BGR được ma trận ảnh I2.
I2 = cv2.cvtColor(I_HSV, cv2.COLOR_HSV2BGR)

# Hiển thị I2.
cv2.imshow('Doi ve BGR', I2)

#5e
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow('Kenh H', Ihsv[:, :, 0])
cv2.imshow('Kenh S', Ihsv[:, :, 1])
cv2.imshow('Kenh V', Ihsv[:, :, 2])
cv2.imshow('HSV', Ihsv)

#Muc xam tb cua kenh V,S,H
print("Muc xam tb kenh V: ", np.mean(Ihsv[:, :, 2]))
print("Muc xam tb kenh S: ", np.mean(Ihsv[:, :, 1]))
print("Muc xam tb kenh H: ", np.mean(Ihsv[:, :, 0]))
 
 
#5g
def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    diff = cmax-cmin
    if cmax == cmin:
        h = 0
    elif cmax == r:
        h = (((g - b)/diff) + 6) * 60
    elif cmax == g:
        h = (((b-r)/diff) + 2) * 60
    elif cmax == b:
        h = (((b-r)/diff) + 4) * 60
    if cmax == 0:
        s = 0
    else:
        s = (diff / cmax) * 100
        v = cmax * 100
    return h, s, v
print(rgb_to_hsv(129, 88, 47))
 
#chuyển đổi ảnh
def bgr2hsv(I):
    if len(I.shape) == 1:
        print("La anh xam khong phai anh rbg")
        return None
    Ihsv = np.zeros((I.shape[0], I.shape[1], 3), dtype=np.uint8)
 
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            r, g, b = I[i, j, 2], I[i, j, 1], I[i, j, 0]
            h, s, v = rgb_to_hsv(r, g, b)
            Ihsv[i, j, 0], Ihsv[i, j, 1], Ihsv[i, j, 2] = h, s, v
    return Ihsv
img_hsv = bgr2hsv(I)
cv2.imshow("Anh bgr sang hsv bang tay", img_hsv)

if cv2.waitKey(0) &0xff == 27:
    cv2.destroyAllWindows()
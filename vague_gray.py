import numpy as np
import cv2
import domi_conv as dc
import domi_expansion as de

#=======================input=========================
img = cv2.imread('Original_picture\\images.jpg')
#=====================================================

#======================轉灰階並重新編碼=================
bimg = de.dm_rgb_to_gray(img)
bimg = np.array(bimg, dtype=np.uint8)
#=====================================================

#=======================設定===========================
kernel = [1, 0, -1,
           2, 0, -2,
           1, 0, -1]

kernel_m = 3
kernel_n = 3

bias = 0

padding = 0
#1白框 0黑框 其他無框
#=====================================================

result_img = dc.dm_rgray(bimg,kernel,kernel_m,kernel_n,bias,padding)


result_img_np = np.array(result_img, dtype=np.uint8)

cv2.imwrite('_conv\\images_sobel.jpg', result_img_np)
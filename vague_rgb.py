import numpy as np
import cv2
import domi_conv as dc

#=======================input=========================
img = cv2.imread('Original_picture\\images.jpg')

kernel = [1/9, 1/9, 1/9,
          1/9, 1/9, 1/9,
          1/9, 1/9, 1/9]

kernel_m = 3
kernel_n = 3

bias = 0

padding = 0
#1白框 0黑框 其他無框
#=====================================================

result_img = dc.dm_rgbc(img,kernel,kernel_m,kernel_n,bias,padding)


result_img_np = np.array(result_img, dtype=np.uint8)

cv2.imwrite('_conv\\images_average.jpg', result_img_np)
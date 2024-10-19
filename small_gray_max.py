import cv2
import numpy as np
import domi_pool as dp
import domi_expansion as de

#=======================input=========================
img = cv2.imread('Original_picture\\images.jpg')
#=====================================================

#======================轉灰階並重新編碼=================
bimg = de.dm_rgb_to_gray(img)
bimg = np.array(bimg, dtype=np.uint8)
#=====================================================

bimg = dp.dm_gray_max_pool(bimg,2,2)
newimg = np.array(bimg, dtype=np.uint8)

cv2.imwrite('_pool\images_gray_max.jpg',newimg)
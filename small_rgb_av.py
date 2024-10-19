import cv2
import numpy as np
import domi_pool as dp

img = cv2.imread('Original_picture\\images.jpg')

img = dp.dm_rgb_av_pool(img,2,2)
newimg = np.array(img, dtype=np.uint8)

cv2.imwrite('_pool\images_rgb_av.jpg',newimg)
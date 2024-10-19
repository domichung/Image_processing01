import cv2
import numpy as np
import domi_pool as dp

img = cv2.imread('Original_picture\\images.jpg')

img = dp.dm_rgb_max_pool(img,2,2)
newimg = np.array(img, dtype=np.uint8)

cv2.imwrite('_pool\images_rgb_max.jpg',newimg)
import numpy as np
import cv2
import domi_expansion as de

img = cv2.imread('Original_picture\\images.jpg')

bimg = de.dm_rgb_to_gray(img)

bimg = np.array(bimg, dtype=np.uint8)

cv2.imwrite('_rgbtogray_pic\\black_images.jpg', bimg)
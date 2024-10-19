import domi_add_sign as ds
import cv2
import numpy as np
import domi_pool as dp

add_sign_photo_locate = 'Original_picture\\images.jpg'
new_sign_photo_locate = 'Original_picture\\sign_images.jpg'
#黑色 0,0,0 白色 255,255,255
change_color = [0,0,0]


img = cv2.imread(add_sign_photo_locate)

sign = cv2.imread('Original_picture\\sign.jpg')

retime = 0

while(1):
    
    if ( ds.test_size(img,sign) ):
        break
    
    newsign = dp.dm_rgb_max_pool(sign,2,2)
    newsign = np.array(newsign, dtype=np.uint8)
    cv2.imwrite('sign_size\\resize_sign.jpg',newsign)

    sign = cv2.imread('sign_size\\resize_sign.jpg')
    retime+=1
    print("已從新設置簽名檔大小"+str(retime)+"次")

    
signimg = ds.dm_sign(img,sign,change_color)

newimg = np.array(signimg, dtype=np.uint8)

#cv2.imshow('My Image', newimg) 
cv2.imwrite(new_sign_photo_locate, newimg)
cv2.waitKey(0)
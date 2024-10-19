import domi_tool as dt

def dm_rgbc(img, kernel, m, n, bias, padding):
    
    height = dt.dm_size(img)
    #m
    width = dt.dm_size(img[0])
    #n
    reimg = dt.dm_cpy(img)

    NOW = 0
    for i in range(0, dt.dm_size(img)):  
        for j in range(0, dt.dm_size(img[i])):
            
            if ( i==0 or j ==0 or j == dt.dm_size(img[i])-1 or i == dt.dm_size(img)-1):
                if (padding == 1):  # 白
                    reimg[i][j] = [255, 255, 255]  
                elif (padding == 0):  # 黑
                    reimg[i][j] = [0, 0, 0]
                continue
            
            reimg[i][j][0] = (
                img[i-1][j-1][0] * kernel[0] +
                img[i-1][j][0] * kernel[1] +
                img[i-1][j+1][0] * kernel[2] +
                img[i][j-1][0] * kernel[3] +
                img[i][j][0] * kernel[4] +
                img[i][j+1][0] * kernel[5] +
                img[i+1][j-1][0] * kernel[6] +
                img[i+1][j][0] * kernel[7] +
                img[i+1][j+1][0] * kernel[8] + bias
            )

            reimg[i][j][1] = (
                img[i-1][j-1][1] * kernel[0] +
                img[i-1][j][1] * kernel[1] +
                img[i-1][j+1][1] * kernel[2] +
                img[i][j-1][1] * kernel[3] +
                img[i][j][1] * kernel[4] +
                img[i][j+1][1] * kernel[5] +
                img[i+1][j-1][1] * kernel[6] +
                img[i+1][j][1] * kernel[7] +
                img[i+1][j+1][1] * kernel[8] + bias
            )

            reimg[i][j][2] = (
                img[i-1][j-1][2] * kernel[0] +
                img[i-1][j][2] * kernel[1] +
                img[i-1][j+1][2] * kernel[2] +
                img[i][j-1][2] * kernel[3] +
                img[i][j][2] * kernel[4] +
                img[i][j+1][2] * kernel[5] +
                img[i+1][j-1][2] * kernel[6] +
                img[i+1][j][2] * kernel[7] +
                img[i+1][j+1][2] * kernel[8] + bias
            )
        
        #print(NOW)
        #NOW += 1
    if (padding == 0 or padding == 1):
        return reimg
    else:
        return dt.dm_small_arr(reimg)


def dm_rgray(img, kernel, m, n, bias, padding):
    
    height = dt.dm_size(img)
    width = dt.dm_size(img[0])
    reimg = dt.dm_cpy(img)

    NOW = 0

    for i in range(0, height):
        for j in range(0, width):

            if ( i==0 or j ==0 or j == dt.dm_size(img[i])-1 or i == dt.dm_size(img)-1):
                if (padding == 1):  # 白
                    reimg[i][j] = 255
                elif (padding == 0):  # 黑
                    reimg[i][j] = 0
                continue

            reimg[i][j] = img[i-1][j-1] * kernel[0] + img[i-1][j] * kernel[1] + img[i-1][j+1] * kernel[2] + \
                         img[i][j-1] * kernel[3] + img[i][j] * kernel[4] + img[i][j+1] * kernel[5] + \
                         img[i+1][j-1] * kernel[6] + img[i+1][j] * kernel[7] + img[i+1][j+1] * kernel[8] + bias
            #print(reimg[i][j])

            if (reimg[i][j]<0):
                reimg[i][j] = -reimg[i][j]
            
   

    if (padding == 0 or padding == 1):
        return reimg
    else:
        return dt.dm_small_arr(reimg)



#kernel = [1/9, 1/9, 1/9,
#          1/9, 1/9, 1/9,
#          1/9, 1/9, 1/9]

#kerrnel = [1, 0, -1,
#           2, 0, -2,
#           1, 0, -1]

#new_conv('images.jpg', kernel, 0, 1)
#testarr = [[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]],[[21,22,23],[24,25,26],[27,28,29]]]

#dm_cc(testarr,0,0,0,0,0)
#print(kernel[6])
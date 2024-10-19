import domi_tool as dt

def dm_rgb_max_pool(img, size, stride):
    
    if (stride != 2 or size != 2):
        print("err")
        return img

    rows = dt.dm_size(img)  
    cols = dt.dm_size(img[0]) if rows > 0 else 0  
    
    new_rows = rows // 2
    new_cols = cols // 2

    if new_rows > 0 and new_cols > 0:
        
        print("success")
        
        cpy = [[[0, 0, 0] for _ in range(new_cols)] for _ in range(new_rows)]
        
        for i in range(new_rows):  
            for j in range(new_cols):  
                
                rmax = img[i*2][j*2][0]  
                
                if img[i*2+1][j*2][0] > rmax:
                    rmax = img[i*2+1][j*2][0]

                if img[i*2][j*2+1][0] > rmax:
                    rmax = img[i*2][j*2+1][0]

                if img[i*2+1][j*2+1][0] > rmax:
                    rmax = img[i*2+1][j*2+1][0]
                
                gmax = img[i*2][j*2][1]  
                
                if img[i*2+1][j*2][1] > gmax:
                    gmax = img[i*2+1][j*2][1]

                if img[i*2][j*2+1][1] > gmax:
                    gmax = img[i*2][j*2+1][1]

                if img[i*2+1][j*2+1][1] > gmax:
                    gmax = img[i*2+1][j*2+1][1]
                
                bmax = img[i*2][j*2][2]  
                
                if img[i*2+1][j*2][2] > bmax:
                    bmax = img[i*2+1][j*2][2]

                if img[i*2][j*2+1][2] > bmax:
                    bmax = img[i*2][j*2+1][2]

                if img[i*2+1][j*2+1][2] > bmax:
                    bmax = img[i*2+1][j*2+1][2]

                cpy[i][j][0] = rmax
                cpy[i][j][1] = gmax
                cpy[i][j][2] = bmax
                
    else:
        cpy = []

    return cpy

def dm_rgb_av_pool(img, size, stride):
    
    if (stride != 2 or size != 2):
        print("err")
        return img

    rows = dt.dm_size(img)  
    cols = dt.dm_size(img[0]) if rows > 0 else 0  
    
    new_rows = rows // 2
    new_cols = cols // 2

    if new_rows > 0 and new_cols > 0:
        
        print("success")
        
        cpy = [[[0, 0, 0] for _ in range(new_cols)] for _ in range(new_rows)]
        
        for i in range(new_rows):  
            for j in range(new_cols):  
                
                rmax = (int(img[i*2][j*2][0]) + int(img[i*2+1][j*2][0]) + int(img[i*2][j*2+1][0]) + int(img[i*2+1][j*2+1][0]))/4
                gmax = (int(img[i*2][j*2][1]) + int(img[i*2+1][j*2][1]) + int(img[i*2][j*2+1][1]) + int(img[i*2+1][j*2+1][1]))/4
                bmax = (int(img[i*2][j*2][2]) + int(img[i*2+1][j*2][2]) + int(img[i*2][j*2+1][2]) + int(img[i*2+1][j*2+1][2]))/4

                cpy[i][j][0] = rmax
                cpy[i][j][1] = gmax
                cpy[i][j][2] = bmax
                
    else:
        cpy = []

    return cpy

def dm_gray_max_pool(img, size, stride):
    
    if (stride != 2 or size != 2):
        print("err")
        return img

    rows = dt.dm_size(img)  
    cols = dt.dm_size(img[0]) if rows > 0 else 0  
    
    new_rows = rows // 2
    new_cols = cols // 2

    if new_rows > 0 and new_cols > 0:
        
        print("success")
        
        cpy = [[[0] for _ in range(new_cols)] for _ in range(new_rows)]
        
        for i in range(new_rows):  
            for j in range(new_cols):  
                
                max = img[i*2][j*2]
                
                if img[i*2+1][j*2] > max:
                    max = img[i*2+1][j*2]

                if img[i*2][j*2+1] > max:
                    max = img[i*2][j*2+1]

                if img[i*2+1][j*2+1] > max:
                    max = img[i*2+1][j*2+1]
                
                cpy[i][j] = max
                
    else:
        cpy = []

    return cpy

def dm_gray_av_pool(img, size, stride):
    
    if (stride != 2 or size != 2):
        print("err")
        return img

    rows = dt.dm_size(img)  
    cols = dt.dm_size(img[0]) if rows > 0 else 0  
    
    new_rows = rows // 2
    new_cols = cols // 2

    if new_rows > 0 and new_cols > 0:
        
        print("success")
        
        cpy = [[[0] for _ in range(new_cols)] for _ in range(new_rows)]
        
        for i in range(new_rows):  
            for j in range(new_cols):  
                
                max = (int(img[i*2][j*2]) + int(img[i*2+1][j*2]) + int(img[i*2][j*2+1]) + int(img[i*2+1][j*2+1]))/4
                
                cpy[i][j] = max
                
    else:
        cpy = []

    return cpy
#img = [
#    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
#    [[13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]],
#    [[25, 26, 27], [28, 29, 30], [31, 32, 33], [34, 35, 36]],
#    [[37, 38, 39], [40, 41, 42], [43, 44, 45], [46, 47, 48]],
#]
#pooled_img = dm_rgb_max_pool(img, 2, 2)
#print(pooled_img)
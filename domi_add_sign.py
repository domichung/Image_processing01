import domi_tool as dt

def dm_sign(img,sign,color):
    
    if ( dt.dm_size(img)<dt.dm_size(sign) or dt.dm_size(img[0])<dt.dm_size(sign[0])):
        print("errr2")
        return img

    print("success")
    for i in range(0, dt.dm_size(img)):  
        for j in range(0, dt.dm_size(img[i])):
            try:
                if (sign[i][j][0]<128 and sign[i][j][1]<128 and sign[i][j][2]<128):
                    img[i][j][0] = color[0]
                    img[i][j][1] = color[1]
                    img[i][j][2] = color[2]
            except:
                continue

    return img

def test_size(img,sign):
    if ( dt.dm_size(img)<dt.dm_size(sign) or dt.dm_size(img[0])<dt.dm_size(sign[0])):
        return 0
    else :
        return 1
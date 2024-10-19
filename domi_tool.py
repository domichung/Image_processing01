def dm_size(arr):
    x = 0
    for w in arr:
        x += 1
    return x

def dm_cpy(arr):
    rows = dm_size(arr)  
    cols = dm_size(arr[0]) if rows > 0 else 0  
    cpy = [[0] * cols for _ in range(rows)]  

    for i in range(rows):
        for j in range(cols):
            cpy[i][j] = arr[i][j]  

    return cpy

def dm_small_arr(arr):
    rows = dm_size(arr)  
    cols = dm_size(arr[0]) if rows > 0 else 0  
    
    new_rows = rows - 2
    new_cols = cols - 2

    if new_rows > 0 and new_cols > 0:
        cpy = [[0] * new_cols for _ in range(new_rows)]
        
        for i in range(1, rows - 1):  
            for j in range(1, cols - 1):  
                cpy[i - 1][j - 1] = arr[i][j]  
    else:
        cpy = []  

    return cpy
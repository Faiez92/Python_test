import numpy as np

def compare_neighbors(arr):
    comp_arr = np.full(arr.shape, False, dtype=bool) 
    arr_height = arr.shape[0]
    arr_width = arr.shape[1]

    for i in range(arr_height): 
        for j in range(arr_width): 

            center = arr[i,j]
            if i == 0: #left 
                left = arr[i,j]
            else:
                left = arr[i-1, j]

            if i == arr_height - 1: #right
                right = arr[i,j]
            else:
                right = arr[i+1,j]

            if j == 0: #up
                up = arr[i,j]
            else:
                up = arr[i, j-1]

            if j == arr_width - 1: #down
                down = arr[i,j]
            else:
                down = arr[i, j+1]

            comp_arr[i,j] = len(set([left, right, up, down, center])) == 1
            if arr[i,j]==False and comp_arr[i,j] == False:
                if comp_arr[i,j+1] == True:
                    return True
                else:
                    return False
            elif arr[i,j]==True and comp_arr[i,j] == False:   
                if comp_arr[i,j+1] == True:
                    return True
                else:
                    return False
    return comp_arr
    
Plateau = np.array ([ [True , False , False , False ] ,
                 [ False , True , True , False ] ])
                 
compare_neighbors(Plateau)
print(compare_neighbors(Plateau))

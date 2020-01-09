''' 
Searches a 2D matrix and returns a local minimum (in the north, south, east,
west directions). 

'''
def 2D_local_min_search(arr): 
    return 2D_local_min_search_h(arr, len(arr) - 1, len(arr[0]) - 1)   

def 2D_local_min_search_h(arr, m, n):

   if is_2D_local_min(arr, m, n):
            return arr[mid_row][mid_col]
    else:
        mid_row = m // 2 
        mid_col = n // 2
        
    

def is_2D_local_min(arr, x, y):
    return arr[x, y] <= arr[x+1, y] and arr[x, y] <= arr[x-1, y] and arr[x, y] <= arr[x, y+1] and arr[x, y-1] <= arr[x, y]
    
print(2D_local_min_search([[4, 5, 10, 19], [10, 2, 100, 300], [30, 40, 50, 600]]) 

''' Visual Reprenstation 
    NW = [0, 0]
    NE = [0, n]
    SE = [m, 0]
    SW = [m, n]
'''
